import { ConferenceModel } from '../interfaces/models/conference'
import { ConferenceServiceI } from './conference'
import * as dotenv from 'dotenv'
import { MongoDb } from '../database/mongodb'
import { ConferenceModelMongo } from '../models/conference'
import { ConferenceDocument } from '../schemas/conferences'

var mongoose = require('mongoose');

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
    //let id= '8bd11a96-ac06-58f5-8727-2ab7f12899c2'
    //let id = '8bd11a96ac0658f587272ab7'
    let id = '8bd11a96ac0658f587272ab7f12899c2'

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
        //console.log(mongoose.Types.ObjectId(id))
        let queriedObj = (await confModelMongo
        .getOne({_id: id }) as ConferenceDocument).toObject()
        console.log(queriedObj)
        // expect(await service.getOne(id)).toEqual(queriedObj)
        // expect(await service.getOne("random-text")).toBeNull()
    })
})

