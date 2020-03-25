<<<<<<< HEAD
import * as dotenv from 'dotenv-safe';
=======
import * as dotenv from 'dotenv';
>>>>>>> 0803630106183622cfcbcc3d332c4214d6a68fc7
/* 
Load the .env file into the process environment variable scope
It's necessary to keep a .env file in the project root
along side package.json
*/
<<<<<<< HEAD
dotenv.config() 
=======
dotenv.config({
    example: './.env'
});
=======
dotenv.config()
>>>>>>> 0803630106183622cfcbcc3d332c4214d6a68fc7
