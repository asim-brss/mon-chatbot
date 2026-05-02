from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  
)

SYSTEM = "Tu es un assistant pédagogique spécialisé en informatique pour lycéens et étudiants en L1. Explique simplement, avec des exemples concrets."

historique = [{"role": "system", "content": SYSTEM}]

print("Chatbot local prêt ! (tape 'quitter' pour arrêter)")

while True:
    user = input("Toi : ")
    if user.lower() == "quitter":
        break

    historique.append({"role": "user", "content": user})

    reponse = client.chat.completions.create(
        model="local-model",  
        messages=historique
    )

    message = reponse.choices[0].message.content
    historique.append({"role": "assistant", "content": message})
    print(f"Bot : {message}\n")
