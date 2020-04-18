import { ConferenceService } from "../interfaces/services/conference"
import { ConferenceController } from "./conference"

describe("Testing for conference contoller" , () => {

    let ServiceMock = jest.fn<ConferenceService , []>()

    let controller = new ConferenceController(new ServiceMock)

    test("Controller instantiation" , () => {
        expect(controller).toBeDefined()
    })
    test("Controller should have the methods defined" , () => {
        expect(controller.getCategories).toBeDefined()
        expect(controller.getConferences).toBeDefined()
        expect(controller.getConferencesFomCategory).toBeDefined()
        expect(controller.getCategories).toBeDefined()
    })
})

