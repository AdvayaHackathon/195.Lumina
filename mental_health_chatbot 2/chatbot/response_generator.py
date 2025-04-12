from chatbot.translation import detect_language, translate_to_english, translate_from_english
import ollama
import re

def generate_response(user_input, relationship, nickname, chat_history, selected_language="en", personality=None):
    try:
        lang = selected_language
        user_input_en = translate_to_english(user_input, source_lang=lang) if lang != "en" else user_input
    except Exception as e:
        print(f"Translation error: {e}")
        user_input_en = user_input

    formatted_history = "\n".join(
        [f"{nickname}: {msg['user']}\n{relationship}: {msg['bot']}" for msg in chat_history]
    )

    # Crisis Mode Detection (Violence-related)
    crisis_keywords = ["kill", "hurt", "revenge", "destroy", "beat", "attack", "murder", "fight"]
    if any(word in user_input.lower().split() for word in crisis_keywords):
        prompt = (
            f"You are {relationship} to {nickname}. Speak with warmth, concern, and care. "
            f"The user is expressing thoughts related to violence or harm. Your goal is to **firmly de-escalate** the situation while providing emotional support. "
            f"Do **not** ask open-ended questions that allow violent thoughts to continue. Instead, immediately shift focus to **calm, logical, and non-violent solutions**. "
            f"Never entertain or encourage violent ideas. Be caring but **clear and firm** that hurting others is unacceptable. "
            f"\nHere is the conversation history so far:\n{formatted_history}\n\n"
            f"{nickname}: {user_input}\n"
            f"{relationship}:"
        )
    else:
        personality_instruction = f"""
        You must behave exactly as per this personality: "{personality}".
        Strict Behavior Rules:
        1. Your tone and personality must stay consistent throughout the conversation.
        2. You are allowed to use emojis in your responses to express emotion naturally — but only if it fits the tone and message. Do not overuse.
        3. NEVER invent people (like Rohan, Michael) or scenarios unless the user clearly mentions them.
        4. Respond only to what the user says. If they say 'Hi', greet them back — no extra emotional talk or random stories.
        5. Do not assume any backstory or situation. Always reply based on user message only.
        6. Use ONLY English. Strictly avoid words like 'beta', 'arre', 'chai', etc."""

        prompt = (
            f"You are {relationship} to {nickname}. "
            f"{personality_instruction} "
            f"\nHere is the conversation history so far:\n{formatted_history}\n\n"
            f"{nickname}: {user_input}\n"
            f"{relationship}:"
        )

    try:
        response = ollama.chat(model="gemma3:latest", messages=[{"role": "user", "content": prompt}])
        ai_response = response["message"]["content"].strip()
        ai_response = refine_response(ai_response)

        if selected_language != "en":
            return translate_from_english(ai_response, selected_language)
        return ai_response

    except Exception as e:
        print(f"Generation error: {e}")
        return ""  # No fallback used anymore

def refine_response(text):
    text = re.sub(r'\b(jaan|bache|mere pyare|ladle|chanda|re|arre|hain na)\b', '', text)
    text = re.sub(r'(\.{2,}|\!{2,})', '.', text)
    text = re.sub(r'\b(Sorry to hear that|I’m sorry)\b', 'I understand', text, flags=re.IGNORECASE)
    text = re.sub(r'\*([^\*]+)\*', r'\1', text)
    return text.strip()
