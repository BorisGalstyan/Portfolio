from database import SessionLocal, Promokod
import json

db = SessionLocal()
modules = ["jurist", "auto", "pc", "home", "med"]
for mod in modules:
    code = f"DEMO{mod.upper()}"
    if not db.query(Promokod).filter(Promokod.code == code).first():
        p = Promokod(code=code, modules=json.dumps([mod]), used=False)
        db.add(p)
db.commit()
print("Демо-промокоды созданы: DEMOJURIST, DEMOAUTO и т.д.")
db.close()
