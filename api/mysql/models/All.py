# -*- coding: utf8 -*-

from sqlalchemy                 import Column, Integer, String, DateTime, Boolean

from ..base                     import Base

class User(Base):
    __tablename__ = 'users'

    id        = Column(Integer, primary_key=True)
    name      = Column(String)
    mail      = Column(String)
    hash      = Column(String)
    d_name    = Column(String)
    d_monkeys = Column(String)
    d_ack     = Column(Boolean)
    created   = Column(DateTime)
    active    = Column(Boolean)
    date      = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), server_onupdate=func.now())

@dataclass
class MP(Base):
    __tablename__ = 'mps'

    id: int
    src_id: int
    src: str
    dst_id: int
    dst: int
    subject: str
    body: str
    date: str

    id      = Column(Integer, primary_key=True)
    src_id  = Column(Integer)
    src     = Column(String)
    dst_id  = Column(Integer)
    dst     = Column(String)
    subject = Column(String)
    body    = Column(String)
    date    = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), server_onupdate=func.now())

@dataclass
class Squad(Base):
    __tablename__ = 'squads'

    id: int
    name: str
    leader: int
    created: str
    date: str

    id      = Column(Integer, primary_key=True)
    name    = Column(String)
    leader  = Column(String)
    created = Column(DateTime)
    date    = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), server_onupdate=func.now())

@dataclass
class MetaWeapons(Base):
    __tablename__ = 'metaWeapons'

    id: int
    name: str
    mastery: int
    onehanded: bool
    ranged: bool
    rng: int
    pas_use: int
    pas_reload: int
    moddable: bool
    caliber: str
    rounds: int
    size: str
    dmg_base: int
    dmg_sneaky: int
    parry: int
    arpen: int
    defcan: int
    min_m: int
    min_r: int
    min_g: int
    min_v: int
    min_p: int
    min_b: int

    id         = Column(Integer, primary_key=True)
    name       = Column(String)
    mastery    = Column(Integer)
    onehanded  = Column(Boolean)
    ranged     = Column(Boolean)
    rng        = Column(Integer)
    pas_use    = Column(Integer)
    pas_reload = Column(Integer)
    moddable   = Column(Boolean)
    caliber    = Column(String)
    rounds     = Column(Integer)
    size       = Column(String)
    dmg_base   = Column(Integer)
    dmg_sneaky = Column(Integer)
    parry      = Column(Integer)
    arpen      = Column(Integer)
    defcan     = Column(Integer)
    min_m      = Column(Integer)
    min_r      = Column(Integer)
    min_g      = Column(Integer)
    min_v      = Column(Integer)
    min_p      = Column(Integer)
    min_b      = Column(Integer)

@dataclass
class MetaArmors(Base):
    __tablename__ = 'metaArmors'

    id: int
    name: str
    tier: bool
    mastery: int
    moddable: bool
    size: str
    arm_p: int
    arm_b: int
    min_m: int
    min_r: int
    min_g: int
    min_v: int
    min_p: int
    min_b: int

    id         = Column(Integer, primary_key=True)
    name       = Column(String)
    mastery    = Column(Integer)
    tier       = Column(Integer)
    moddable   = Column(Boolean)
    size       = Column(String)
    arm_p      = Column(Integer)
    arm_b      = Column(Integer)
    min_m      = Column(Integer)
    min_r      = Column(Integer)
    min_g      = Column(Integer)
    min_v      = Column(Integer)
    min_p      = Column(Integer)
    min_b      = Column(Integer)

@dataclass
class Items(Base):
    __tablename__ = 'items'

    id: int
    metatype: str
    metaid: int
    bearer: int
    bound: bool
    bound_type: str
    modded: bool
    mods: str
    state: int
    rarity: int
    offsetx: int
    offsety: int
    date: str

    id         = Column(Integer, primary_key=True)
    metatype   = Column(String)
    metaid     = Column(Integer)
    bearer     = Column(Integer)
    bound      = Column(Boolean)
    bound_type = Column(String)
    modded     = Column(Boolean)
    mods       = Column(String)
    state      = Column(Integer)
    rarity     = Column(Integer)
    offsetx    = Column(Integer)
    offsety    = Column(Integer)
    date       = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), server_onupdate=func.now())

@dataclass
class Map(Base):
    __tablename__ = 'maps'

    id: int
    type: str
    size: int
    data: bool
    date: str

    id         = Column(Integer, primary_key=True)
    type       = Column(String)
    size       = Column(String)
    data       = Column(String)
    date       = Column(DateTime(timezone=True), nullable=False, server_default=func.now(), server_onupdate=func.now())