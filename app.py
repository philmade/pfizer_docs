# Create a flask sql-alchemy model for sqlite with the attributes below
# "STUDYID","USUBJID","SUBJID","SITEID","TRTP","TRTPN","TRTA","TRTAN","ISDTC","ADT","ADY","AVISIT","AVISITN","VISIT","VISITNUM","PARCAT1","PARCAT1N","PARAM","PARAMN","PARAMCD","AVAL","AVALC","BASE","BASEC","BASETYPE","ABLFL","APSBLFL","ABLPBLFL","DTYPE","R2BASE","SRCDOM","SRCVAR","SRCSEQ","ANL01FL","ANL03FL","ANL04FL","ISLLOQ","ISSTRESC","EVIMMFL","AAIMMFL","BSSERON","BSSEROC","APERIOD","APERIODC","APERSDTM","APEREDTM","BASE4F","R2BASE4F","FOLD4FL","ISTSTDTL","AGE","AGEU","SEX","SEXN","RACE","RACEN","RANDFL","SAFFL","ARM","ARMCD","ACTARM","ACTARMCD","TRTSDT","TRTEDT","TRTSTM","TRTETM","TRT01A","TRT01AN","TRT02A","TRT02AN","TRT01P","TRT01PN","TRT02P","TRT02PN","TR01SDT","TR01STM","TR01SDTM","TR01EDT","TR01ETM","TR01EDTM","TR02SDT","TR02STM","TR02SDTM","TR02EDT","TR02ETM","TR02EDTM","COHORTN","COHORT","VAX101DT","VAX102DT","VAX10UDT","VAX201DT","VAX202DT","AAI01FL","EVAL02FL","AAI02FL","EVAL01FL","DOSALVL","DOSALVLN","DOSPLVL","DOSPLVLN","AGEGR1","AGEGR1N","AGEGR2","AGEGR2N","AGEGR4","AGEGR4N","PHASE","PHASEN","COVBLST","HIVFL","PEDIMMFL","EV1MD2FL","AGETR01","VAX101","VAX102","VAX10U","VAX201","VAX202","VAX20U","VAX20UDT","UNBLNDDT","MULENRFL","RAND1FL","TRTSDTM","TRTEDTM"

# "STUDYID","USUBJID","SUBJID","SITEID","TRTP","TRTPN","TRTA","TRTAN","ISDTC","ADT","ADY","AVISIT","AVISITN","VISIT","VISITNUM","PARCAT1","PARCAT1N","PARAM","PARAMN","PARAMCD","AVAL","AVALC","BASE","BASEC","BASETYPE","ABLFL","APSBLFL","ABLPBLFL","DTYPE","R2BASE","SRCDOM","SRCVAR","SRCSEQ","ANL01FL","ANL03FL","ANL04FL","ISLLOQ","ISSTRESC","EVIMMFL","AAIMMFL","BSSERON","BSSEROC","APERIOD","APERIODC","APERSDTM","APEREDTM","BASE4F","R2BASE4F","FOLD4FL","ISTSTDTL","AGE

class Subject(db.Model):
    __tablename__ = 'subjects'
    usubjid = db.Column(db.Integer, primary_key=True)


class Study(db.Model):
    __tablename__ = 'studies'
    id = db.Column(db.Integer, primary_key=True)
    studyid = db.Column(db.String(64), unique=True)
    usubjid = db.Column(db.String(64), unique=True)
    subjid = db.Column(db.String(64), unique=True)
    siteid = db.Column(db.String(64), unique=True)
    trtp = db.Column(db.String(64), unique=True)
    trtpn = db.Column(db.String(64), unique=True)
    trta = db.Column(db.String(64), unique=True)
    trtan = db.Column(db.String(64), unique=True)
    isdtc = db.Column(db.String(64), unique=True)
    adt = db.Column(db.String(64), unique=True)
    ady = db.Column(db.String(64), unique=True)
    avisit = db.Column(db.String(64), unique=True)
    avisitn = db.Column(db.String(64), unique=True)
    visit = db.Column(db.String(64), unique=True)
    visitnum = db.Column(db.String(64), unique=True)
    parcat1 = db.Column(db.String(64), unique=True)
    parcat1n = db.Column(db.String(64), unique=True)
    param = db.Column(db.String(64), unique=True)
    paramn = db.Column(db.String(64), unique=True)
    paramcd = db.Column(db.String(64), unique=True)
    aval = db.Column(db.String(64), unique=True)
    avalc = db.Column(db.String(64), unique=True)
    base = db.Column(db.String(64), unique=True)
    basec = db.Column(db.String(64), unique=True)