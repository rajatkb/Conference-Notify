import {Logger} from './log'


test("Testing for environment variable" , () => {
    expect(process.env.LOG_FOLDER).toBeDefined()
    expect(process.env.LOG_LEVEL).toBeDefined()
} )

test("Testing for Logger " , () => {
    let logger = new Logger("test");
    let log = logger.getLogger()
    expect(log).toBeDefined()
    expect(log.info).toBeDefined()
    expect(log.warn).toBeDefined()
    expect(log.debug).toBeDefined()
    expect(log.error).toBeDefined()
})

