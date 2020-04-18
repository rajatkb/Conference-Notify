import { ConferenceModel } from '../interfaces/models/conference'
import { ConferenceServiceI } from './conference'

describe("Testing Conferences Service Implementation " ,() => {
    let ModelMock = jest.fn<ConferenceModel , []>()
    let model = new ModelMock()
    let categories = ["category1" , "category2"]
    model.getCategories = jest.fn(() => Promise.resolve(["category1" , "category2"]))
    model.getConferences = jest.fn( () => Promise.resolve([]) )


    let service = new ConferenceServiceI(model)

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
    })
})

