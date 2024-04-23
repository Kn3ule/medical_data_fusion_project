import os
from sqlalchemy import Column, ForeignKey, create_engine
from sqlalchemy.sql.sqltypes import Integer, String, BigInteger, DateTime, Float,Boolean
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine(os.getenv("POSTGRES_URL"))
base = declarative_base()
conn = engine.connect()
Session = sessionmaker()
my_session = Session(bind=engine)


class MetaData(base):
    __tablename__ = 'metadata'

    ecg_id = Column(Integer, primary_key=True,autoincrement=True)
    patient_id = Column(Float)
    age = Column(Float)
    sex = Column(Float)
    height = Column(Float)
    weight = Column(Float)
    nurse = Column(Float)
    site = Column(Float)
    device = Column(String)
    recording_date = Column(DateTime)
    report = Column(String)
    scp_codes = Column(String)
    heart_axis = Column(String)
    infarction_stadium1 = Column(String)
    infarction_stadium2 = Column(String)
    validated_by = Column(Float)
    second_opinion = Column(Boolean)
    initial_autogenerated_report = Column(Boolean)
    validated_by_human = Column(Boolean)
    baseline_drift = Column(String)
    static_noise = Column(String)
    burst_noise = Column(String)
    electrodes_problems = Column(String)
    extra_beats = Column(String)
    pacemaker = Column(String)
    strat_fold = Column (Float)
    filename_lr = Column(String)
    filename_hr = Column(String)

class ScpStatements(base):

    __tablename__ = 'scpstatements'

    name = Column(String, primary_key=True)
    description = Column(String)
    diagnostic = Column(Float)
    form = Column(Float)
    rhythm = Column(Float)
    diagnostic_class = Column(String)
    diagnositc_subclass = Column(String)
    statement_category = Column(String)
    scp_ecg_statement_description = Column(String)
    aha_code = Column(Float)
    aecg_refid = Column(String)
    cdisc_code = Column(String)
    dicom_code = Column(String)


    
def create_tables():
    base.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()