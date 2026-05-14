from question_model import Question

question_data_raw = [
    {
        "question": "Is AWS more economical than traditional data centers for scalable workloads?",
        "correct_answer": True,
        "explanation": "AWS can be more economical due to its pay-as-you-go pricing model and scalability."
    },
    {
        "question": "Does AWS Storage Gateway help integrate on-premises applications with AWS cloud storage?",
        "correct_answer": True,
        "explanation": "AWS Storage Gateway connects on-premises environments with cloud storage seamlessly."
    },
    {
        "question": "Is AWS Marketplace a digital catalog with thousands of software listings?",
        "correct_answer": True,
        "explanation": "AWS Marketplace allows users to find, buy, and deploy software on AWS."
    },
    {
        "question": "Does Amazon VPC allow users to create a logically isolated section of AWS?",
        "correct_answer": True,
        "explanation": "Amazon VPC lets users define their own virtual network within AWS."
    },
    {
        "question": "Are AWS customers responsible for maintaining physical hardware?",
        "correct_answer": False,
        "explanation": "AWS handles physical infrastructure; customers manage applications and data."
    },
    {
        "question": "Does Amazon CloudFront use edge locations to reduce latency?",
        "correct_answer": True,
        "explanation": "CloudFront caches content at edge locations to deliver it faster."
    },
    {
        "question": "Does Multi-Factor Authentication (MFA) add an extra security layer?",
        "correct_answer": True,
        "explanation": "MFA requires multiple verification methods, increasing security."
    },
    {
        "question": "Can AWS X-Ray trace requests through an application?",
        "correct_answer": True,
        "explanation": "AWS X-Ray helps monitor and debug distributed applications."
    },
    {
        "question": "Can Amazon SNS send notifications to users or systems?",
        "correct_answer": True,
        "explanation": "Amazon SNS is used for messaging and notifications."
    },
    {
        "question": "Does AWS Billing provide pricing and usage information?",
        "correct_answer": True,
        "explanation": "AWS Billing helps track costs and monitor usage."
    }
]

# Convert raw dicts into Question objects
question_data = [Question(**q) for q in question_data_raw]