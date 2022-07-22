from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from data.config import *


class DataBase:
    def __init__(self):
        self.pool = Union[Pool, None]

    async def conf(self):
        self.pool = await asyncpg.create_pool(
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            database=DB_NAME
        )

    async def execute(self, sql, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False,
                      executemany: bool = False):

        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(sql, *args)
                elif fetchval:
                    result = await connection.fetchval(sql, *args)
                elif fetchrow:
                    result = await connection.fetchrow(sql, *args)
                elif execute:
                    result = await connection.execute(sql, *args)
                elif executemany:
                    result = await connection.executemany(sql, *args)
            return result

    async def create_table_users(self):
        sql = """
                CREATE TABLE IF NOT EXISTS Users(
                    user_id BIGINT NOT NULL UNIQUE,
                    region VARCHAR(30)
                )
"""
        await self.execute(sql, execute=True)

    async def insert_user(self, chat_id):
        sql = """
                INSERT INTO USERS (user_id)
                VALUES ($1)
                ON CONFLICT (user_id) DO NOTHING;
"""
        await self.execute(sql, chat_id, execute=True)

    async def user_info(self, chat_id):
        sql = """
                SELECT region FROM Users WHERE user_id=$1;
"""
        return await self.execute(sql, chat_id, fetchval=True)

    async def update_user(self, region, chat_id):
        sql = """
                UPDATE USERS SET region = $1
                WHERE user_id = $2
"""
        await self.execute(sql, region, chat_id, execute=True)

    async def get_users(self):
        sql = """
            SELECT user_id FROM users        
"""
        return await self.execute(sql, fetch=True)
