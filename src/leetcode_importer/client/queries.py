QUESTION_LIST_QUERY = """
    query($skip: Int!) {
        problemsetQuestionListV2(
            categorySlug: ""
            limit: 20
            skip: $skip
        ) {
            questions {
                questionFrontendId
                titleSlug
            }
        }
    }
"""

QUESTION_DATA_QUERY = """
    query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            topicTags {
                name
            }
            content
            codeSnippets {
                langSlug
                code
            }
        }
    }
"""
