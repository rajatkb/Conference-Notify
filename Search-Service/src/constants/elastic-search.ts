const ES_TYPE_STRING = {
    type: 'text',
};

const ES_TYPE_STRING_WITH_KEYWORD = {
    type: 'text',
    fields: {
        keyword: {
            type: 'keyword',
            ignore_above: 256,
            normalizer: 'lowercase_normalizer',
        },
    },
};

const ES_TYPE_DATE = {
    type: 'date',
};

const ES_TYPE_KEYWORD = {
    type: 'keyword',
};

const ES_TYPE_STRING_WITH_KEYWORD_AND_ACCENT_INSENSITIVE_ANALYZER = {
    type: 'text',
    fields: {
        keyword: {
            type: 'keyword',
            ignore_above: 256,
            normalizer: 'lowercase_normalizer',
        },
        insensitive: {
            type: 'text',
            analyzer: 'custom_accent_insensitive_analyzer',
        },
    },
};

export const ELASTIC_SEARCH_INDICES = {
    conference: {
        name: process.env.ELASTICSEARCH_INDEX_CONFERENCE,
        document: {
            mappings: {
                properties: {
                    title: ES_TYPE_STRING_WITH_KEYWORD_AND_ACCENT_INSENSITIVE_ANALYZER,
                    url: ES_TYPE_STRING_WITH_KEYWORD,
                    deadline: ES_TYPE_DATE,
                    categories: ES_TYPE_KEYWORD,
                    dateRange: ES_TYPE_DATE,
                    finalDue: ES_TYPE_STRING_WITH_KEYWORD,
                    location: ES_TYPE_STRING_WITH_KEYWORD,
                    notificationDue: ES_TYPE_DATE,
                    bulkText: ES_TYPE_STRING_WITH_KEYWORD_AND_ACCENT_INSENSITIVE_ANALYZER,
                },
            },
            settings: {
                analysis: {
                    normalizer: {
                        lowercase_normalizer: {
                            type: 'custom',
                            char_filter: [],
                            filter: ['lowercase'],
                        },
                    },
                    analyzer: {
                        custom_accent_insensitive_analyzer: {
                            type: 'custom',
                            tokenizer: 'standard',
                            filter: ['asciifolding'],
                        },
                    },
                },
            },
        },
    },
};
