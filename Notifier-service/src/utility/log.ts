import winston from 'winston';

// const FileConfig = (filename:string) =>{ 
//     return {
//             level: process.env.LOG_LEVEL,
//             filename: `${process.env.LOG_FOLDER}/${filename}.log`,
//             handleExceptions: true,
//             json: true,
//             colorize: false,
//             timestamp:true
//         } 
// }

// const ConsoleConfig = {
//     level: process.env.LOG_LEVEL,
//     handleExceptions: true,
//     colorize: true,
//     prettyPrint: true
// }


export class Logger{


    private logger:winston.Logger; 
    constructor(filename:string){
        this.logger = winston.createLogger({
            level: process.env.LOG_LEVEL,
            transports: [
                new winston.transports.Console({ format: winston.format.colorize({all:true}),}),
                new winston.transports.File({ filename: `${process.env.LOG_FOLDER}/${filename}.log` })
            ] , 

            format: winston.format.combine(
                         winston.format.label({
                            label: filename
                         }),
                         
                         winston.format.timestamp(),
                         winston.format.printf((info) => {
                             return `${info.timestamp} - ${info.label}:[${info.level}]: ${info.message}`;
                         })
                     )

        })
    }    

    getLogger():winston.Logger{
        return this.logger;
    }
    
}







