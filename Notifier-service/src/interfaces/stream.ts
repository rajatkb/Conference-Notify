import { Observable } from "rxjs";



/**
 * Stream interface responsible for representing
 * a observable that can be subscribed and being listened by a 
 * listener
 * @export
 * @interface Stream
 */
export interface Stream{
    getStream():Observable<any>;
    getInsertStream():Observable<any>;
    getUpdateStream():Observable<any>;
    getDeleteStream():Observable<any>;
    getReplaceStream():Observable<any>;
}