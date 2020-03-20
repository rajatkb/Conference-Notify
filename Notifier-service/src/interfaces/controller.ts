import { Service }  from './services'

export abstract class Controller {
    protected success = (fun: string, info: any) => `Recieved request for ${fun}  from: ${info}`
    protected fail = (fun: string, info: any, err: any) => `Failed at request for ${fun} from : ${info} : Error encountered : ${err}`

    protected successResponse = (payload:any) => {
        return {
            status: 200,
            payload: payload
        }
    }

    protected failResponse = () => {
        return {
            status:404,
            payload:null
        }
    }

    constructor(service:Service){};
}