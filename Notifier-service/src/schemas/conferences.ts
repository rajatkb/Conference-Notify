import { Metadata } from './metadata';
import { Schema, Document } from 'mongoose'; 

type Conference = {
    title:string;
    url:string;
    deadline:Date;
    metadata?:{
        [tag:string]:Metadata
    };
    
    categories?:Array<string>;
    dateRange?:Array<Date>;
    finalDue?:string;
    location?:string;
    notificationDue?:Date;
    bulkText?:string; // optional field
}

type mongoQueryType = {
    _id?: string;
}

interface ConferenceDocument extends Document {
    title:string;
    url:string;
    deadline:Date;
    metadata?:{
        [tag:string]:Metadata
    };
    
    categories?:Array<string>;
    dateRange?:Array<Date>;
    finalDue?:string;
    location?:string;
    notificationDue?:Date;
    bulkText?:string; // optional field
} 

let ConferenceSchema = new Schema({
    title:{type:String , required:true},
    url:{type:String , required:true},
    deadline:{type:Date , required:true},
} , {strict : false});

export {Conference , ConferenceDocument , ConferenceSchema, mongoQueryType}



