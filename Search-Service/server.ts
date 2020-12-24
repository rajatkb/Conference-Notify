import * as dotenv from 'dotenv-safe';
import { createESIndex } from './src/services/es-index';
/* 
Load the .env file into the process environment variable scope
It's necessary to keep a .env file in the project root
along side package.json
*/
dotenv.config({
    example: './.env'
});

createESIndex();