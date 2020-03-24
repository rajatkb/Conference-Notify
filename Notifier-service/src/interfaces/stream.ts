import { Observable } from "rxjs";
import { injectable } from "inversify";


export interface Stream{
    getStream():Observable<any>
}