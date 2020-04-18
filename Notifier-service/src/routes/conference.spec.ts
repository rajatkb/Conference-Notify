import { ConferenceController } from "../controllers/conference"
import { ConferenceRoute } from "./conference"

describe("Route testing" , () => {
    let MockController = jest.fn<ConferenceController , []>()
    let mock = new MockController()
    mock.getOne = jest.fn()
    mock.getCategories = jest.fn()
    mock.getConferences = jest.fn()
    mock.getConferencesFomCategory = jest.fn()

    let route = new ConferenceRoute(mock)

    test("Route insantiation" , () => {
        expect(route.getRouter).toBeDefined()
    })
    
})