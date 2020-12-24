import * as elasticSearch from 'elasticsearch';
import { ELASTIC_SEARCH_INDICES } from '../constants/elastic-search';

const esConfig: elasticSearch.ConfigOptions = {
    host: process.env.ELASTICSEARCH_HOST || '',
};

const client = new elasticSearch.Client(esConfig);

export const createESIndex = async () => {
    await client.indices.delete({
        index: process.env.ELASTICSEARCH_INDEX_CONFERENCE || '',
        ignore: [400, 404],
    });
    await client.indices.create({
        index: process.env.ELASTICSEARCH_INDEX_CONFERENCE || '',
        // not ignoring the error so that we may get to know if there is an issue while creating the index
        // ignore: [400],
        body: {
            ...ELASTIC_SEARCH_INDICES.conference.document,
        },
    });
};
