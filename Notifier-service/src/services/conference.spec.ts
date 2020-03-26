import { ConferenceModel } from '../interfaces/models/conference'
import { ConferenceServiceI } from './conference'
import { async } from 'rxjs/internal/scheduler/async'

describe("Testing Conferences Service Implementation " ,() => {
    let ModelMock = jest.fn<ConferenceModel , []>()
    let model = new ModelMock()
    let categories = ["category1" , "category2"]
    model.getCategories = jest.fn(() => Promise.resolve(["category1" , "category2"]))

    
    let service = new ConferenceServiceI(model)

    test("service instantiation" , () => {
        expect(service).toBeDefined()
    })

    test("service calls" , async () => {
        expect(service.getCategories).toBeDefined()
        expect(await service.getCategories()).toEqual(categories)
        expect(service.getConferencesFromCategory).toBeDefined()
        expect(service.getConferences).toBeDefined()
        expect(service.getOne).toBeDefined()
    })



})

