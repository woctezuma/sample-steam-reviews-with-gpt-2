import sys

import steamreviews
from langdetect import detect, DetectorFactory, lang_detect_exception


def download_recent_reviews(app_id):
    request_params = dict()
    request_params['filter'] = 'all'
    request_params['day_range'] = '28'
    request_params['language'] = 'english'

    review_dict, _ = steamreviews.download_reviews_for_app_id(app_id=app_id,
                                                              chosen_request_params=request_params)

    reviews = review_dict['reviews']

    return reviews


def detect_language(reviews,
                    review_ids=None,
                    verbose=True):
    if review_ids is None:
        review_ids = reviews.keys()

    detected_languages = dict()

    DetectorFactory.seed = 0

    for count, review_id in enumerate(review_ids):
        if verbose and (count + 1) % 1000 == 0:
            print('Reviews processed by langdetect: {}/{}.'.format(count + 1, len(review_ids)))

        review_content = reviews[review_id]['review']

        try:
            detected_languages[review_id] = detect(review_content)
        except lang_detect_exception.LangDetectException:
            detected_languages[review_id] = 'unknown'
            print(review_content)

    return detected_languages


def filter_out_reviews_not_written_in_english(reviews,
                                              review_ids=None,
                                              language_str='english'):
    if review_ids is None:
        review_ids = reviews.keys()

    print('Filtering out reviews which were not written in {}.'.format(language_str))
    review_ids = list(filter(lambda x: reviews[x]['language'] == language_str, review_ids))

    print('#reviews = {}'.format(len(review_ids)))

    return review_ids


def filter_out_short_reviews(reviews,
                             review_ids=None,
                             length_threshold=150):
    if review_ids is None:
        review_ids = reviews.keys()

    print('Filtering out reviews with strictly fewer than {} characters.'.format(length_threshold))
    review_ids = list(filter(lambda x: len(reviews[x]['review']) >= length_threshold, review_ids))

    print('#reviews = {}'.format(len(review_ids)))

    return review_ids


def filter_out_reviews_not_detected_as_written_in_english(reviews,
                                                          review_ids=None,
                                                          expected_language_code='en'):
    if review_ids is None:
        review_ids = reviews.keys()

    detected_languages = detect_language(reviews, review_ids)

    print('Filtering out reviews which were not detected as written in {}.'.format(expected_language_code))
    review_ids = list(filter(lambda x: detected_languages[x] == expected_language_code, review_ids))

    print('#reviews = {}'.format(len(review_ids)))

    return review_ids


def filter_reviews(reviews):
    review_ids = list(reviews.keys())
    print('#reviews = {}'.format(len(review_ids)))

    review_ids = filter_out_reviews_not_written_in_english(reviews, review_ids)
    review_ids = filter_out_short_reviews(reviews, review_ids)
    review_ids = filter_out_reviews_not_detected_as_written_in_english(reviews, review_ids)

    return review_ids


def get_data_folder():
    data_folder = 'data/'

    return data_folder


def get_txt_output_file_name(app_id):
    output_text_file_name = get_data_folder() + str(app_id) + '.txt'
    return output_text_file_name


def trim_review_content(review_content):
    # Remove empty lines

    review_content_chunks = [
        line.strip() for line in review_content.split('\n')
        if len(line.strip()) > 0
    ]

    trimmed_review_content = '\n'.join(review_content_chunks)

    return trimmed_review_content


def concatenate_reviews(output_text_file_name,
                        reviews,
                        review_ids=None,
                        remove_empty_lines=True):
    if review_ids is None:
        review_ids = reviews.keys()

    # Append to a large list

    review_list = []

    for review_id in review_ids:
        review_content = reviews[review_id]['review']

        if remove_empty_lines:
            trimmed_review_content = trim_review_content(review_content)
        else:
            trimmed_review_content = review_content

        review_list.append(trimmed_review_content)

    # Concatenate as a large str

    line_separator = '\n'

    concatenated_reviews = line_separator.join(review_list)

    # Save to disk

    with open(output_text_file_name, 'w', encoding='utf8') as f:
        print(concatenated_reviews, file=f)

    return


def apply_workflow_for_app_id(app_id):
    output_text_file_name = get_txt_output_file_name(app_id)

    reviews = download_recent_reviews(app_id)

    review_ids = filter_reviews(reviews)

    concatenate_reviews(output_text_file_name, reviews, review_ids)

    return


def main(argv):
    if len(argv) == 0:
        app_id = 583950
        print('No detected command-line argument. AppID automatically set to {}.'.format(app_id))
    else:
        app_id = argv[0]
        print('A command-line argument is detected. AppID set to {}.'.format(app_id))

    apply_workflow_for_app_id(app_id)

    return


if __name__ == '__main__':
    main(sys.argv[1:])
