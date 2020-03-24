import { Conference } from '../schemas/conferences'
import { ConferenceService } from '../interfaces/services/conference';
import { Controller } from '../interfaces/controller';
import { Response, Request } from 'express'
import { Logger } from '../utility/log';
import { injectable } from 'inversify';


@injectable()
export class ConferenceController extends Controller {

    private logger = new Logger(this.constructor.name).getLogger();

    constructor(private conferenceService: ConferenceService) {
        super(conferenceService)
    }



    getOne = async (request: Request, response: Response) => {
        let requester = request.ip;
        let category: string = request.params.category;
        this.logger.info(this.success("getOne", requester))
        try {

            let result = await this.conferenceService.getOne();
            response.json(this.successResponse(result));
        }
        catch (e) {
            this.logger.error(this.fail("getOne" , requester , e));
            response.json(this.failResponse())
        }
    }

    getConferences = async (request: Request, response: Response) => {
        let requester = request.ip;
        let offset: string = request.params.offset;
        let count: string = request.params.count;
        try {
            let offseti = Number.parseFloat(offset);
            let counti =  Number.parseFloat(count);
            if( Number.isNaN(offseti) || Number.isNaN(counti)){
                throw new Error("Illegal arguments given for route , redirecting")
            }
            this.logger.info(this.success("getConference", requester))
            try {

                let result: Conference[] = await this.conferenceService
                                                    .getConferences(
                                                        offseti , 
                                                        counti);
                response.json(this.successResponse(result));
            }
            catch (e) {
                this.logger.error(this.fail("getConference" , requester , e));
                response.json(this.failResponse())
            }
        } catch (e) {
            this.logger.warn(this.fail("getConference", requester, e))
            response.redirect('/')
        }
    }

    getConferencesFomCategory = async (request: Request, response: Response) => {
        let offset: string = request.params.offset;
        let count: string = request.params.count;
        let category: string = request.params.category;
        let requester = request.connection.address
        try {
            let offseti = Number.parseFloat(offset);
            let counti =  Number.parseFloat(count);
            if( Number.isNaN(offseti) || Number.isNaN(counti)){
                throw new Error("Illegal arguments given for route , redirecting")
            }
            this.logger.info(this.success("getConferenceFromCategory", requester))
            try {
                let result: Conference[] = await this.conferenceService
                                                    .getConferencesFromCategory(
                                                        category,
                                                        offseti , 
                                                        counti);
                response.json(this.successResponse(result));
            }
            catch (e) {
                this.logger.error(this.fail("getConferenceFromCategory" , requester , e));
                response.json(this.failResponse())
            }

        } catch (e) {
            this.logger.error(this.fail("getConferenceFromCategory", requester, e))
            response.redirect('/')
        }
    }


    getCategories = async (request: Request, response: Response) => {
        let category: string = request.params.category;
        let requester = request.connection.address
        try {
            this.logger.info(this.success("getCategories", requester))
            let result: Array<String> = await this.conferenceService.getCategories();
            this.successResponse(result)
        } catch (e) {
            this.logger.error(this.fail("getCategories" , requester , e));
            response.json(this.failResponse())
        }
    }
}