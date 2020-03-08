let FileConfig = (filename:string) =>{ 
    return {
            level: process.env.LOG_LEVEL,
            filename: `${process.env.LOG_FOLDER}/${filename}.log`,
            handleExceptions: true,
            json: true,
            colorize: false,
        } 
}

let ConsoleConfig = {
    level: process.env.LOG_LEVEL,
    handleExceptions: true,
    json: false,
    colorize: true,
}

export { FileConfig , ConsoleConfig}