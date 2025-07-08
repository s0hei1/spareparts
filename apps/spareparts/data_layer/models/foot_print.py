from sqlalchemy import Column, DateTime, Integer, ForeignKey
from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr

class FootPrint:

    @declared_attr
    def creation_date_time(self):
        return Column(DateTime, default=datetime.utcnow, nullable=False)

    @declared_attr
    def creation_user_id(self):
        return Column(Integer, ForeignKey('user.id'), nullable=False)

    @declared_attr
    def last_modification_date_time(self):
        return Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    @declared_attr
    def last_modification_user_id(self):
        return Column(Integer, ForeignKey('user.id'), nullable=False)