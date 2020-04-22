import { ConferenceModel } from '../interfaces/models/conference'
import { ConferenceServiceI } from './conference'

describe("Testing Conferences Service Implementation " ,() => {
    let ModelMock = jest.fn<ConferenceModel , []>()
    let model = new ModelMock()
    let conferenceModelMongoMock = jest.fn()
    let confModelMongo = new conferenceModelMongoMock()
    let categories = ["category1" , "category2"]
    let mongoData: any = {title: "t",
                    url: "u",
                    deadline: new Date()}
    let mongoRes: any = {toObject: jest.fn(()=>mongoData) }
    confModelMongo.getOne = jest.fn(()=> Promise.resolve(mongoRes))
    model.getCategories = jest.fn(() => Promise.resolve(["category1" , "category2"]))
    model.getConferences = jest.fn( () => Promise.resolve([]) )
    let service = new ConferenceServiceI(model,confModelMongo)
    let id= '8bd11a96-ac06-58f5-8727-2ab7f12899c2'

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
        expect(await service.getOne(id)).toEqual(mongoData)
    })
})

