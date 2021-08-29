#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:23:28 2017

@author: inoueshinichi
"""

""" sqlAlchemy_ORM.py """

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

conn = sa.create_engine('sqlite:///zoo.db')

Base = declarative_base()

class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)
    
    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages
        
    def __repr__(self):
        return "<Zoo({}, {}, {})>".format(self.critter, self.count,
                    self.damages)
        
        


# データベースとテーブルの作成
Base.metadata.create_all(conn)

# データの挿入（Pythonオブジェクト作成）
first = Zoo('duck', 10, 0.0)
second = Zoo('bear', 2, 1000.0)
third = Zoo('weasel', 1, 2000.0)

# 表示
first

# データベースとのセッション（やりとり）
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
session = Session()

session.add(first)
session.add_all([second, third])

# 強制的に処理を完了させる
session.commit()



