import { ConferenceModel } from '../interfaces/models/conference'
import { ConferenceServiceI } from './conference'
import * as dotenv from 'dotenv'
import { MongoDb } from '../database/mongodb'
import { ConferenceModelMongo } from '../models/conference'
import { ConferenceDocument } from '../schemas/conferences'

describe("Testing Conferences Service Implementation " ,() => {
    dotenv.config()
    let ModelMock = jest.fn<ConferenceModel , []>()
    let model = new ModelMock()
    let categories = ["category1" , "category2"]
    model.getCategories = jest.fn(() => Promise.resolve(["category1" , "category2"]))
    model.getConferences = jest.fn( () => Promise.resolve([]) )
    const mongo = new MongoDb()
    const confModelMongo = new ConferenceModelMongo(mongo)
    let queryKey = "url"
    let queryValue = "https://www.kdd.org/kdd2020/"
    let service = new ConferenceServiceI(model,confModelMongo)


    test("service instantiation" , () => {
        expect(service).toBeDefined()
    })

    test("service calls" , async () => {
        expect(service.getCategories).toBeDefined()
        expect(await service.getCategories()).toEqual(categories)
        expect(service.getConferencesFromCategory).toBeDefined()
        expect(service.getConferences).toBeDefined()
        expect(await service.getConferences(1 , 2)).toEqual([])
        expect(service.getOne).toBeDefined()
        let queriedObj = (await confModelMongo
        .getOne({url: queryValue }) as ConferenceDocument).toObject()
        expect(await service.getOne(queryKey,queryValue)).toEqual(queriedObj)
        expect(await service.getOne(queryKey,"random-text")).toBeNull()
    })
})

