import { Conference } from '../schemas/conferences'
import { ConferenceService } from '../interfaces/services/conference';
import { Controller } from '../interfaces/controller';
import { Response, Request } from 'express'
import { Logger } from '../utility/log';


export class ConferenceController extends Controller {

    private logger = new Logger(this.constructor.name).getLogger();

    constructor(private conferenceService: ConferenceService) {
        super(conferenceService)
    }

    private success = (fun: string, info: any) => `Recieved request for ${fun}  from: ${info}`
    private fail = (fun: string, info: any, err: any) => `Failed at request for ${fun} from : ${info} : Error encountered : ${err}`

    getOne = async (request: Request, response: Response) => {
        let requester = request.ip ;
        let category: string = request.params.category;
        try {
            this.logger.info(this.success("getOne", requester))
            let result = await this.conferenceService.getOne();
            response.json({
                status: 200,
                payload: result
            });
        } catch (e) {
            this.logger.error(this.fail("getOne", requester, e))
            response.redirect('/')
        }
    }

    getConferences = async (request: Request, response: Response) => {
        let requester = request.connection.address
        let offset: string = request.params.offset;
        let count: string = request.params.count;
        try {
            this.logger.info(this.success("getConference", requester))
            let result: Conference[] = await this.conferenceService
                .getConferences(
                    Number.parseFloat(offset),
                    Number.parseFloat(count));
            response.json({
                status: 200,
                payload: result
            });
        } catch (e) {
            this.logger.error(this.fail("getConference", requester, e))
            response.redirect('/')
        }
    }

    getConferencesFomCategory = async (request: Request, response: Response) => {
        let offset: string = request.params.offset;
        let count: string = request.params.count;
        let category: string = request.params.category;
        let requester = request.connection.address
        try {
            this.logger.info(this.success("getConferenceFromCategory", requester))
            let result: Conference[] = await this.conferenceService.
                getConferencesFromCategory(
                    category,
                    Number.parseFloat(offset),
                    Number.parseFloat(count));
            response.json({
                status: 200,
                payload: result
            });
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
            response.json(result);
        } catch (e) {
            
        }
    }
}