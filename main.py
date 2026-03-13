from fastapi import FastAPI,UploadFile
import analyzer
import ai_helper


app = FastAPI()
@app.post("/csv-insight")

async def csv_insights(file:UploadFile):
    analyze_data = analyzer.analyze_csv(file)
    insights = ai_helper.generate_insights(analyze_data)

    return {
        "columns":analyze_data,
        "insights":insights
    }