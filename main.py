from resume_screening.inference import run_resume_screening
from sentiment_analysis.inference import run_sentiment_analysis
import argparse
import os

def main():
    print("\n🔍 Running Resume Screening...\n")
    run_resume_screening(
        "resume_screening/examples/sample_resume_1.txt",
        "resume_screening/job_description.txt"
    )

    print("\n💬 Running Sentiment Analysis...\n")
    run_sentiment_analysis("sentiment_analysis/examples/feedback_1.txt")

if __name__ == "__main__":
    # Optional CLI override
    parser = argparse.ArgumentParser(description="HR AI Assistant")

    parser.add_argument(
        "--resume", type=str,
        help="Path to resume file (.txt or .pdf)",
        default="resume_screening/examples/sample_resume_1.txt"
    )
    parser.add_argument(
        "--jd", type=str,
        help="Path to job description file (.txt)",
        default="resume_screening/job_description.txt"
    )
    parser.add_argument(
        "--feedback", type=str,
        help="Path to employee feedback file (.txt)",
        default="sentiment_analysis/examples/feedback_1.txt"
    )

    args = parser.parse_args()

    print("\n🔍 Running Resume Screening...\n")
    run_resume_screening(args.resume, args.jd)

    print("\n💬 Running Sentiment Analysis...\n")
    run_sentiment_analysis(args.feedback)
