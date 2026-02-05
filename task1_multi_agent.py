# TASK 1: Simple Multi-Agent Simulation

# Agent 1: Data Collector
def data_collector(company):
    data = f"{company} is financially stable. Stock growth is moderate."
    return data

# Agent 2: Analyst
def analyst(data):
    analysis = f"Based on data: {data}. Risk is low and outlook is positive."
    return analysis

# Orchestrator
company_name = "Tesla"
collected_data = data_collector(company_name)
final_result = analyst(collected_data)

print("Collected Data:")
print(collected_data)
print("\nFinal Analysis:")
print(final_result)
