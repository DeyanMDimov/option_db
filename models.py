from sqlalchemy import Column, Boolean, Date, Double, Integer, DateTime, Numeric, PrimaryKeyConstraint, SmallInteger, String, Time, Uuid, Index, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from pydantic import BaseModel, ConfigDict
from decimal import Decimal
from typing import Optional
from datetime import datetime, date
import uuid

class Base(DeclarativeBase):
    pass


class EodDataSymbol(Base):
    __tablename__ = 'eod_data_symbol'
    __table_args__ = (
        PrimaryKeyConstraint('eod_id', name='eod_data_symbol_pkey'),
    )

    eod_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    eod_symbol: Mapped[Optional[str]] = mapped_column(String(20))
    eod_currency: Mapped[Optional[int]] = mapped_column(SmallInteger)
    eod_exchange: Mapped[Optional[int]] = mapped_column(SmallInteger)
    eod_vendor: Mapped[Optional[str]] = mapped_column(String(3))
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean)
    eod_sedol: Mapped[Optional[str]] = mapped_column(String(7))
    start_date: Mapped[Optional[date]] = mapped_column(Date)
    end_date: Mapped[Optional[date]] = mapped_column(Date)
    change_date: Mapped[Optional[date]] = mapped_column(Date)
    notes: Mapped[Optional[str]] = mapped_column(String(255))


class EodHistPrice(Base):
    __tablename__ = 'eod_hist_price'
    __table_args__ = (
        PrimaryKeyConstraint('eod_id', 'eod_hist_date', name='eod_hist_price_pkey'),
    )

    eod_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    eod_hist_date: Mapped[date] = mapped_column(Date, primary_key=True)
    open: Mapped[Optional[Decimal]] = mapped_column(Numeric(8, 0))
    high: Mapped[Optional[Decimal]] = mapped_column(Numeric(8, 0))
    low: Mapped[Optional[Decimal]] = mapped_column(Numeric(8, 0))
    close: Mapped[Optional[Decimal]] = mapped_column(Numeric(8, 0))
    adj_close: Mapped[Optional[Decimal]] = mapped_column(Numeric(8, 0))


class EodDataSymbol(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    eod_id: int 
    eod_symbol: Optional[str]
    eod_currency: Optional[int]
    eod_exchange: Optional[int]
    eod_vendor: Optional[str]
    is_active: Optional[bool]
    eod_sedol: Optional[str] 
    start_date: Optional[date]
    end_date: Optional[date]
    change_date: Optional[date]
    notes: Optional[str]

class EodHistPrice(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    eod_id: int
    eod_hist_date: date
    open: Optional[Decimal]
    high: Optional[Decimal]
    low: Optional[Decimal]
    close: Optional[Decimal]
    adj_close: Optional[Decimal]

class EtfCompPrices(Base):
    __tablename__ = 'etf_comp_prices'
    __table_args__ = (
        PrimaryKeyConstraint('comp_cc_id', 'comp_sedol', name='etf_comp_prices_pkey'),
    )

    comp_cc_id: Mapped[str] = mapped_column(String(15), primary_key=True)
    comp_sedol: Mapped[str] = mapped_column(String(7), primary_key=True)
    close_price: Mapped[Optional[float]] = mapped_column(Double(53))
    close_price_date: Mapped[Optional[date]] = mapped_column(Date)
    close_price_time: Mapped[Optional[datetime.time]] = mapped_column(Time(True))
    currency: Mapped[Optional[str]] = mapped_column(String)
    real_time: Mapped[Optional[bool]] = mapped_column(Boolean)


class EtfComponents(Base):
    __tablename__ = 'etf_components'
    __table_args__ = (
        PrimaryKeyConstraint('comp_uid', name='etf_components_pkey'),
    )

    etf_name: Mapped[str] = mapped_column(String(5))
    comp_cc_id: Mapped[str] = mapped_column(String(15))
    comp_uid: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True)
    comp_sedol: Mapped[Optional[str]] = mapped_column(String(7))
    qty: Mapped[Optional[float]] = mapped_column(Double(53))


class EtfProfiles(Base):
    __tablename__ = 'etf_profiles'
    __table_args__ = (
        PrimaryKeyConstraint('etf_ticker', name='etf_profiles_pkey'),
    )

    etf_ticker: Mapped[str] = mapped_column(String(5), primary_key=True)
    fund_sponsor: Mapped[Optional[str]] = mapped_column(String(20))
    basket_type: Mapped[Optional[str]] = mapped_column(String(8))
    calculation_unit: Mapped[Optional[int]] = mapped_column(Integer)
    iiv_type: Mapped[Optional[str]] = mapped_column(String(15))



class Symbol(Base):
    __tablename__ = 'symbol'
    __table_args__ = (
        PrimaryKeyConstraint('stock_id', name='symbol_pkey'),
    )

    cc_id: Mapped[str] = mapped_column(String(20))
    stock_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    ticker: Mapped[Optional[str]] = mapped_column(String(15))
    instr_type: Mapped[Optional[str]] = mapped_column(String)
    exchange: Mapped[Optional[str]] = mapped_column(String(15))
    sedol: Mapped[Optional[str]] = mapped_column(String(7))
    eod_id: Mapped[Optional[str]] = mapped_column(String(15))
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean)

class SymbolModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    cc_id: str
    stock_id: int
    ticker: Optional[str]
    instr_type: Optional[str]
    is_active: Optional[bool]
    exchange: Optional[str]
    sedol: Optional[str]
    eod_id: Optional[str]



class OptionsContract(Base):
    __tablename__ = 'options_contracts'
    

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    underlying_symbol: Mapped[str] = mapped_column(String(10), nullable=False, index=True)
    option_symbol: Mapped[str] = mapped_column(String(30), nullable=False, unique=True, index=True)
    contract_type: Mapped[str] = mapped_column(String(4), nullable=False)  # 'CALL' or 'PUT'
    strike_price: Mapped[Decimal] = mapped_column(Numeric(12, 4), nullable=False, index=True)
    expiration_date: Mapped[date] = mapped_column(Date, nullable=False, index=True)
    is_index_option: Mapped[bool] = mapped_column(Boolean, default=False)
    date_available: Mapped[Optional[date]] = mapped_column(Date)
    days_to_expiration: Mapped[Optional[int]] = mapped_column(SmallInteger)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    market_data = relationship("OptionsMarketData", back_populates="contract")
    

    __table_args__ = (
        Index('idx_contracts_underlying_expiry', 'underlying_symbol', 'expiration_date'),
        Index('idx_contracts_underlying_strike', 'underlying_symbol', 'strike_price'),
        Index('idx_contracts_chain_lookup', 'underlying_symbol', 'expiration_date', 'contract_type'),
        Index('idx_contracts_active', 'is_active'),
    )