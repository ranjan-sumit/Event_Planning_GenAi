# import streamlit as st
# from langchain import OpenAI, LLMChain
# from langchain.prompts import PromptTemplate
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

# # Function to query the LangChain assistant
# def query_assistant(user_input, api_key):
#     llm = OpenAI(api_key=api_key)  # Use the provided OpenAI API key
#     prompt_template = PromptTemplate(
#         template="You are an event planning assistant. Respond to the following question: {question}",
#         input_variables=["question"]
#     )
#     chain = LLMChain(llm=llm, prompt=prompt_template)
#     return chain.run({"question": user_input})

# # Function to generate and display a word cloud
# def show_word_cloud(prompts):
#     text = ' '.join(prompts)
#     wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
#     plt.figure(figsize=(10, 5))
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis('off')
#     st.pyplot(plt)

# # Dummy venue data
# venue_data = {
#     "Corporate": [
#         {"name": "Venue A", "capacity": 100, "location": "Downtown"},
#         {"name": "Venue B", "capacity": 50, "location": "Uptown"},
#         {"name": "Venue C", "capacity": 150, "location": "City Center"},
#     ],
#     "Birthday": [
#         {"name": "Birthday Venue A", "capacity": 30, "location": "Near Park"},
#         {"name": "Birthday Venue B", "capacity": 20, "location": "Coastal Area"},
#     ],
#     "Wedding": [
#         {"name": "Wedding Venue A", "capacity": 200, "location": "Beachside"},
#         {"name": "Wedding Venue B", "capacity": 150, "location": "Garden"},
#     ]
# }

# # Function to get venue suggestions based on event type and capacity
# def get_venue_suggestions(event_type, capacity):
#     suggestions = []
#     for venue in venue_data.get(event_type, []):
#         if venue["capacity"] >= capacity:
#             suggestions.append(f"{venue['name']} (Capacity: {venue['capacity']}, Location: {venue['location']})")
#     return suggestions

# # Main application function
# def main():
#     st.title("Event Planning Assistant")

#     # Input for OpenAI API key
#     api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    
#     if api_key:
#         # Simple user input for name (simulate authentication)
#         user_name = st.text_input("Enter your name:", "")
#         if user_name:
#             st.session_state.user_name = user_name
#             st.success(f"Welcome, {user_name}!")

#         # Initialize session states for chat history and prompts
#         if 'history' not in st.session_state:
#             st.session_state.history = []
#         if 'prompts' not in st.session_state:
#             st.session_state.prompts = []

#         # User input for questions
#         user_input = st.text_input("Ask your event planning question:")
#         if st.button("Submit"):
#             if user_input:
#                 response = query_assistant(user_input, api_key)
#                 st.session_state.history.append((user_input, response))
#                 st.session_state.prompts.append(user_input)

#         # Display chat history
#         for user_question, assistant_response in st.session_state.history:
#             st.write(f"**You:** {user_question}")
#             st.write(f"**Assistant:** {assistant_response}")

#         # Generate and display word cloud
#         if st.session_state.prompts:
#             show_word_cloud(st.session_state.prompts)

#         # Venue suggestions based on user input
#         event_type = st.selectbox("Select event type:", ["Corporate", "Birthday", "Wedding"])
#         capacity = st.number_input("Enter the number of guests:", min_value=1)
#         if st.button("Get Venue Suggestions"):
#             suggestions = get_venue_suggestions(event_type, capacity)
#             if suggestions:
#                 st.write("### Venue Suggestions:")
#                 for suggestion in suggestions:
#                     st.write(f"- {suggestion}")
#             else:
#                 st.write("No suitable venues found.")

# # Run the application
# if __name__ == "__main__":
#     main()


# import streamlit as st
# from langchain import OpenAI, LLMChain
# from langchain.prompts import PromptTemplate
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

# # Function to query the LangChain assistant
# def query_assistant(user_input, api_key):
#     llm = OpenAI(api_key=api_key)  # Use the provided OpenAI API key
#     prompt_template = PromptTemplate(
#         template="You are an event planning assistant. Respond to the following question: {question}",
#         input_variables=["question"]
#     )
#     chain = LLMChain(llm=llm, prompt=prompt_template)
#     return chain.run({"question": user_input})

# # Function to generate and display a word cloud
# def show_word_cloud(prompts):
#     text = ' '.join(prompts)
#     wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
#     plt.figure(figsize=(10, 5))
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis('off')
#     st.pyplot(plt)

# # Dummy venue data
# venue_data = {
#     "Corporate": [
#         {"name": "Venue A", "capacity": 100, "location": "Downtown"},
#         {"name": "Venue B", "capacity": 50, "location": "Uptown"},
#         {"name": "Venue C", "capacity": 150, "location": "City Center"},
#     ],
#     "Birthday": [
#         {"name": "Birthday Venue A", "capacity": 30, "location": "Near Park"},
#         {"name": "Birthday Venue B", "capacity": 20, "location": "Coastal Area"},
#     ],
#     "Wedding": [
#         {"name": "Wedding Venue A", "capacity": 200, "location": "Beachside"},
#         {"name": "Wedding Venue B", "capacity": 150, "location": "Garden"},
#     ]
# }

# # Function to get venue suggestions based on event type and capacity
# def get_venue_suggestions(event_type, capacity):
#     suggestions = []
#     for venue in venue_data.get(event_type, []):
#         if venue["capacity"] >= capacity:
#             suggestions.append(f"{venue['name']} (Capacity: {venue['capacity']}, Location: {venue['location']})")
#     return suggestions

# # Main application function
# def main():
#     st.title("Event Planning Assistant")

#     # Input for OpenAI API key
#     api_key = st.text_input("Enter your OpenAI API Key:", type="password")
    
#     if api_key:
#         # Simple user input for name (simulate authentication)
#         user_name = st.text_input("Enter your name:", "")
#         if user_name:
#             st.session_state.user_name = user_name
#             st.success(f"Welcome, {user_name}!")

#         # Initialize session states for chat history and prompts
#         if 'history' not in st.session_state:
#             st.session_state.history = []
#         if 'prompts' not in st.session_state:
#             st.session_state.prompts = []

#         # User input for questions
#         user_input = st.text_input("Ask your event planning question:")
#         if st.button("Submit"):
#             if user_input:
#                 response = query_assistant(user_input, api_key)
#                 st.session_state.history.append((user_input, response))
#                 st.session_state.prompts.append(user_input)

#         # Display the most recent result in a container with copy-to-clipboard
#         if st.session_state.history:
#             recent_question, recent_response = st.session_state.history[-1]
#             with st.container():
#                 st.markdown("### Recent Result")
#                 st.write(f"**You:** {recent_question}")
#                 st.write(f"**Assistant:** {recent_response}")
#                 # Clipboard functionality
#                 st.markdown(f"""
#                     <div class="custom-container">
#                         <p id="recent-response">{recent_response}</p>
#                         <button class="copy-btn" onclick="copyToClipboard('recent-response')">Copy to Clipboard</button>
#                     </div>
#                 """, unsafe_allow_html=True)

#         # Expandable section for past interactions
#         if st.session_state.history:
#             with st.expander("Chat History"):
#                 for user_question, assistant_response in st.session_state.history[:-1]:  # Skip the most recent
#                     st.write(f"**You:** {user_question}")
#                     st.write(f"**Assistant:** {assistant_response}")

#         # Generate and display word cloud
#         if st.session_state.prompts:
#             show_word_cloud(st.session_state.prompts)

#         # Venue suggestions based on user input
#         event_type = st.selectbox("Select event type:", ["Corporate", "Birthday", "Wedding"])
#         capacity = st.number_input("Enter the number of guests:", min_value=1)
#         if st.button("Get Venue Suggestions"):
#             suggestions = get_venue_suggestions(event_type, capacity)
#             if suggestions:
#                 st.write("### Venue Suggestions:")
#                 for suggestion in suggestions:
#                     st.write(f"- {suggestion}")
#             else:
#                 st.write("No suitable venues found.")

# # Custom CSS for beautiful containers
# st.markdown("""
#     <style>
#     .custom-container {
#         background-color: #f9f9f9;
#         border-radius: 15px;
#         padding: 20px;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#         font-family: 'Helvetica', sans-serif;
#         font-size: 16px;
#         margin-bottom: 20px;
#     }
#     .custom-container h3 {
#         color: #4CAF50;
#         margin-bottom: 10px;
#     }
#     .custom-container p {
#         color: #333;
#         font-size: 14px;
#     }
#     .copy-btn {
#         background-color: #4CAF50;
#         color: white;
#         padding: 8px 16px;
#         border: none;
#         border-radius: 5px;
#         cursor: pointer;
#         margin-top: 10px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # JavaScript for copy-to-clipboard functionality
# st.markdown("""
#     <script>
#     function copyToClipboard(id) {
#         var copyText = document.getElementById(id);
#         navigator.clipboard.writeText(copyText.innerText);
#         alert("Response copied to clipboard!");
#     }
#     </script>
# """, unsafe_allow_html=True)

# # Run the application
# if __name__ == "__main__":
#     main()


# import streamlit as st
# from langchain import OpenAI, LLMChain
# from langchain.prompts import PromptTemplate
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

# # Function to query the LangChain assistant
# def query_assistant(user_input, api_key):
#     llm = OpenAI(api_key=api_key)  # Use the provided OpenAI API key
#     prompt_template = PromptTemplate(
#         template="You are an event planning assistant. Respond to the following question: {question}",
#         input_variables=["question"]
#     )
#     chain = LLMChain(llm=llm, prompt=prompt_template)
#     return chain.run({"question": user_input})

# # Function to generate and display a word cloud
# def show_word_cloud(prompts):
#     text = ' '.join(prompts)
#     wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
#     plt.figure(figsize=(10, 5))
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis('off')
#     st.pyplot(plt)

# # Dummy venue data
# venue_data = {
#     "Corporate": [
#         {"name": "Venue A", "capacity": 100, "location": "Downtown"},
#         {"name": "Venue B", "capacity": 50, "location": "Uptown"},
#         {"name": "Venue C", "capacity": 150, "location": "City Center"},
#     ],
#     "Birthday": [
#         {"name": "Birthday Venue A", "capacity": 30, "location": "Near Park"},
#         {"name": "Birthday Venue B", "capacity": 20, "location": "Coastal Area"},
#     ],
#     "Wedding": [
#         {"name": "Wedding Venue A", "capacity": 200, "location": "Beachside"},
#         {"name": "Wedding Venue B", "capacity": 150, "location": "Garden"},
#     ]
# }

# # Function to get venue suggestions based on event type and capacity
# def get_venue_suggestions(event_type, capacity):
#     suggestions = []
#     for venue in venue_data.get(event_type, []):
#         if venue["capacity"] >= capacity:
#             suggestions.append(f"{venue['name']} (Capacity: {venue['capacity']}, Location: {venue['location']})")
#     return suggestions

# # Main application function
# def main():
#     st.title("Event Planning Assistant")

#     # Sidebar with app description
#     st.sidebar.title("About This App")
#     st.sidebar.write("""
#         This Event Planning Assistant helps you manage and organize various events seamlessly. 
#         You can ask questions about event planning, view past interactions, generate word clouds 
#         based on your queries, and get venue suggestions based on your requirements.
#     """)

#     # Input for OpenAI API key
#     api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
    
#     # Initialize session states for chat history and prompts
#     if 'history' not in st.session_state:
#         st.session_state.history = []
#     if 'prompts' not in st.session_state:
#         st.session_state.prompts = []

#     # Create tabs for different functionalities
#     tab1, tab2, tab3, tab4 = st.tabs(["Search and Check Results", "Chat History", "Word Cloud", "Venue Suggestions"])

#     with tab1:
#         st.header("Search and Check Results")
#         # User input for questions
#         user_input = st.text_input("Ask your event planning question:")
#         if st.button("Submit"):
#             if user_input:
#                 response = query_assistant(user_input, api_key)
#                 st.session_state.history.append((user_input, response))
#                 st.session_state.prompts.append(user_input)

#         # Display the most recent result in a container
#         if st.session_state.history:
#             recent_question, recent_response = st.session_state.history[-1]
#             with st.container():
#                 st.markdown("### Recent Result")
#                 st.write(f"**You:** {recent_question}")
#                 st.write(f"**Assistant:** {recent_response}")

#     with tab2:
#         st.header("Chat History")
#         # Expandable section for past interactions
#         if st.session_state.history:
#             with st.expander("View Past Interactions"):
#                 for user_question, assistant_response in st.session_state.history:
#                     st.write(f"**You:** {user_question}")
#                     st.write(f"**Assistant:** {assistant_response}")
#         else:
#             st.write("No chat history available.")

#     with tab3:
#         st.header("Word Cloud")
#         # Generate and display word cloud
#         if st.session_state.prompts:
#             show_word_cloud(st.session_state.prompts)
#         else:
#             st.write("No prompts available for word cloud generation.")

#     with tab4:
#         st.header("Venue Suggestions")
#         # Venue suggestions based on user input
#         event_type = st.selectbox("Select event type:", ["Corporate", "Birthday", "Wedding"])
#         capacity = st.number_input("Enter the number of guests:", min_value=1)
#         if st.button("Get Venue Suggestions"):
#             suggestions = get_venue_suggestions(event_type, capacity)
#             if suggestions:
#                 st.write("### Venue Suggestions:")
#                 for suggestion in suggestions:
#                     st.write(f"- {suggestion}")
#             else:
#                 st.write("No suitable venues found.")

# # Run the application
# if __name__ == "__main__":
#     main()


# import streamlit as st
# from langchain import OpenAI, LLMChain
# from langchain.prompts import PromptTemplate
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

# # Function to query the LangChain assistant
# def query_assistant(user_input, api_key):
#     llm = OpenAI(api_key=api_key)
#     prompt_template = PromptTemplate(
#         template="You are an event planning assistant. Respond to the following question: {question}",
#         input_variables=["question"]
#     )
#     chain = LLMChain(llm=llm, prompt=prompt_template)
#     return chain.run({"question": user_input})

# # Function to generate and display a word cloud
# def show_word_cloud(prompts):
#     text = ' '.join(prompts)
#     wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
#     plt.figure(figsize=(10, 5))
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis('off')
#     st.pyplot(plt)

# # Dummy venue data
# venue_data = {
#     "Corporate": [
#         {"name": "Venue A", "capacity": 100, "location": "Downtown"},
#         {"name": "Venue B", "capacity": 50, "location": "Uptown"},
#         {"name": "Venue C", "capacity": 150, "location": "City Center"},
#     ],
#     "Birthday": [
#         {"name": "Birthday Venue A", "capacity": 30, "location": "Near Park"},
#         {"name": "Birthday Venue B", "capacity": 20, "location": "Coastal Area"},
#     ],
#     "Wedding": [
#         {"name": "Wedding Venue A", "capacity": 200, "location": "Beachside"},
#         {"name": "Wedding Venue B", "capacity": 150, "location": "Garden"},
#     ]
# }

# # Function to get venue suggestions based on event type and capacity
# def get_venue_suggestions(event_type, capacity):
#     suggestions = []
#     for venue in venue_data.get(event_type, []):
#         if venue["capacity"] >= capacity:
#             suggestions.append(f"{venue['name']} (Capacity: {venue['capacity']}, Location: {venue['location']})")
#     return suggestions

# # Custom CSS for the app
# st.markdown("""
#     <style>
#     body {
#         font-family: 'Helvetica', sans-serif;
#         background-color: #f9f9f9;
#     }
#     .container {
#         background-color: #ffffff;
#         border-radius: 15px;
#         padding: 20px;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#         margin: 20px 0;
#     }
#     .custom-button {
#         background-color: #4CAF50;
#         color: white;
#         padding: 10px 15px;
#         border: none;
#         border-radius: 5px;
#         cursor: pointer;
#     }
#     .custom-button:hover {
#         background-color: #45a049;
#     }
#     .question {
#         font-weight: bold;
#         color: #333;
#     }
#     .response {
#         background-color: #e7f3fe;
#         border-left: 6px solid #2196F3;
#         padding: 10px;
#         margin-top: 5px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Main application function
# def main():
#     st.title("Event Planning Assistant")

#     # Sidebar with app description
#     st.sidebar.title("About This App")
#     st.sidebar.write("""
#         This Event Planning Assistant helps you manage and organize various events seamlessly. 
#         You can ask questions about event planning, view past interactions, generate word clouds 
#         based on your queries, and get venue suggestions based on your requirements.
#     """)

#     # Input for OpenAI API key
#     api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
    
#     # Initialize session states for chat history and prompts
#     if 'history' not in st.session_state:
#         st.session_state.history = []
#     if 'prompts' not in st.session_state:
#         st.session_state.prompts = []

#     # Create tabs for different functionalities
#     tab1, tab2, tab3, tab4 = st.tabs(["Search and Check Results", "Chat History", "Word Cloud", "Venue Suggestions"])

#     with tab1:
#         st.header("Search and Check Results")
#         # User input for questions
#         user_input = st.text_input("Ask your event planning question:")
        
#         if st.button("Submit", key="submit_btn"):
#             if user_input:
#                 response = query_assistant(user_input, api_key)
#                 st.session_state.history.append((user_input, response))
#                 st.session_state.prompts.append(user_input)

#         # Display the most recent result in a styled container
#         if st.session_state.history:
#             recent_question, recent_response = st.session_state.history[-1]
#             with st.container():
#                 st.markdown("<div class='container'>", unsafe_allow_html=True)
#                 st.markdown("### Recent Result")
#                 st.markdown(f"<p class='question'>**You:** {recent_question}</p>", unsafe_allow_html=True)
#                 st.markdown(f"<div class='response'><strong>Assistant:</strong> {recent_response}</div>", unsafe_allow_html=True)
#                 st.markdown("</div>", unsafe_allow_html=True)

#     with tab2:
#         st.header("Chat History")
#         # Expandable section for past interactions
#         if st.session_state.history:
#             with st.expander("View Past Interactions"):
#                 for user_question, assistant_response in st.session_state.history:
#                     st.write(f"**You:** {user_question}")
#                     st.write(f"**Assistant:** {assistant_response}")
#         else:
#             st.write("No chat history available.")

#     with tab3:
#         st.header("Word Cloud")
#         # Generate and display word cloud
#         if st.session_state.prompts:
#             show_word_cloud(st.session_state.prompts)
#         else:
#             st.write("No prompts available for word cloud generation.")

#     with tab4:
#         st.header("Venue Suggestions")
#         # Venue suggestions based on user input
#         event_type = st.selectbox("Select event type:", ["Corporate", "Birthday", "Wedding"])
#         capacity = st.number_input("Enter the number of guests:", min_value=1)
#         if st.button("Get Venue Suggestions"):
#             suggestions = get_venue_suggestions(event_type, capacity)
#             if suggestions:
#                 st.write("### Venue Suggestions:")
#                 for suggestion in suggestions:
#                     st.write(f"- {suggestion}")
#             else:
#                 st.write("No suitable venues found.")

# # Run the application
# if __name__ == "__main__":
#     main()


# import streamlit as st
# from langchain import OpenAI, LLMChain
# from langchain.prompts import PromptTemplate
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# import random

# # Function to query the LangChain assistant
# def query_assistant(user_input, api_key):
#     llm = OpenAI(api_key=api_key)
#     prompt_template = PromptTemplate(
#         template="You are an event planning assistant. Respond to the following question: {question}",
#         input_variables=["question"]
#     )
#     chain = LLMChain(llm=llm, prompt=prompt_template)
#     return chain.run({"question": user_input})

# # Function to generate and display a word cloud
# def show_word_cloud(prompts):
#     text = ' '.join(prompts)
#     wordcloud = WordCloud(width=600, height=300, background_color='Black').generate(text)
#     plt.figure(figsize=(10, 5))
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis('off')
#     st.pyplot(plt)

# # Dummy venue data
# venue_data = {
#     "Corporate": [
#         {"name": "Venue A", "capacity": 100, "location": "Downtown"},
#         {"name": "Venue B", "capacity": 50, "location": "Uptown"},
#         {"name": "Venue C", "capacity": 150, "location": "City Center"},
#     ],
#     "Birthday": [
#         {"name": "Birthday Venue A", "capacity": 30, "location": "Near Park"},
#         {"name": "Birthday Venue B", "capacity": 20, "location": "Coastal Area"},
#     ],
#     "Wedding": [
#         {"name": "Wedding Venue A", "capacity": 200, "location": "Beachside"},
#         {"name": "Wedding Venue B", "capacity": 150, "location": "Garden"},
#     ]
# }

# # Function to get venue suggestions based on event type and capacity
# def get_venue_suggestions(event_type, capacity):
#     suggestions = []
#     for venue in venue_data.get(event_type, []):
#         if venue["capacity"] >= capacity:
#             suggestions.append(f"{venue['name']} (Capacity: {venue['capacity']}, Location: {venue['location']})")
#     return suggestions

# # Function to generate a random color
# def random_color():
#     return f'#{random.randint(0, 0xFFFFFF):06x}'

# # Custom CSS for the app
# st.markdown("""
#     <style>
#     body {
#         font-family: 'Helvetica', sans-serif;
#         background-color: #f9f9f9;
#     }
#     .container {
#         background-color: #ffffff;
#         border-radius: 15px;
#         padding: 20px;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#         margin: 20px 0;
#     }
#     .custom-button {
#         background-color: #4CAF50;
#         color: white;
#         padding: 10px 15px;
#         border: none;
#         border-radius: 5px;
#         cursor: pointer;
#     }
#     .custom-button:hover {
#         background-color: #45a049;
#     }
#     .question {
#         font-weight: bold;
#         color: #333;
#     }
#     .response {
#         background-color: #e7f3fe;
#         border-left: 6px solid #2196F3;
#         padding: 10px;
#         margin-top: 5px;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Main application function
# def main():
#     st.title("Event Planning Assistant")

#     # Sidebar with app description
#     st.sidebar.title("About This App")
#     st.sidebar.write("""
#         This Event Planning Assistant helps you manage and organize various events seamlessly. 
#         You can ask questions about event planning, view past interactions, generate word clouds 
#         based on your queries, and get venue suggestions based on your requirements.
#     """)

#     # Input for OpenAI API key
#     api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
    
#     # Initialize session states for chat history and prompts
#     if 'history' not in st.session_state:
#         st.session_state.history = []
#     if 'prompts' not in st.session_state:
#         st.session_state.prompts = []

#     # Create tabs for different functionalities
#     tab1, tab2, tab3, tab4 = st.tabs(["Search and Check Results", "Chat History", "Word Cloud", "Venue Suggestions"])

#     with tab1:
#         st.header("Search and Check Results")
#         # User input for questions
#         user_input = st.text_input("Ask your event planning question:")
        
#         if st.button("Submit", key="submit_btn"):
#             if user_input:
#                 response = query_assistant(user_input, api_key)
#                 st.session_state.history.append((user_input, response))
#                 st.session_state.prompts.append(user_input)

#         # Display the most recent result in a styled container
#         if st.session_state.history:
#             recent_question, recent_response = st.session_state.history[-1]
#             with st.container():
#                 st.markdown("<div class='container'>", unsafe_allow_html=True)
#                 st.markdown("### Recent Result")
#                 st.markdown(f"<p class='question'>**You:** {recent_question}</p>", unsafe_allow_html=True)
#                 st.markdown(f"<div class='response'><strong>Assistant:</strong> {recent_response}</div>", unsafe_allow_html=True)
#                 st.markdown("</div>", unsafe_allow_html=True)

#     with tab2:
#         st.header("Chat History")
#         # Expandable section for past interactions
#         if st.session_state.history:
#             with st.expander("View Past Interactions"):
#                 for user_question, assistant_response in st.session_state.history:
#                     st.markdown(f"<p class='question'>**You:** {user_question}</p>", unsafe_allow_html=True)
#                     # Apply random color for assistant's response
#                     assistant_color = random_color()
#                     st.markdown(f"<div class='response' style='border-left: 6px solid {assistant_color};'><strong>Assistant:</strong> {assistant_response}</div>", unsafe_allow_html=True)
#         else:
#             st.write("No chat history available.")

#     with tab3:
#         st.header("Word Cloud")
#         # Generate and display word cloud
#         if st.session_state.prompts:
#             show_word_cloud(st.session_state.prompts)
#         else:
#             st.write("No prompts available for word cloud generation.")

#     with tab4:
#         st.header("Venue Suggestions")
#         # Venue suggestions based on user input
#         event_type = st.selectbox("Select event type:", ["Corporate", "Birthday", "Wedding"])
#         capacity = st.number_input("Enter the number of guests:", min_value=1)
#         if st.button("Get Venue Suggestions"):
#             suggestions = get_venue_suggestions(event_type, capacity)
#             if suggestions:
#                 st.write("### Venue Suggestions:")
#                 for suggestion in suggestions:
#                     st.write(f"- {suggestion}")
#             else:
#                 st.write("No suitable venues found.")

# # Run the application
# if __name__ == "__main__":
#     main()


import streamlit as st
from langchain import OpenAI, LLMChain
from langchain.prompts import PromptTemplate
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random
# Set Streamlit app to full width
st.set_page_config(layout="wide")
# Function to query the LangChain assistant
def query_assistant(user_input, api_key):
    llm = OpenAI(api_key=api_key)
    prompt_template = PromptTemplate(
        template="You are an event planning assistant. Respond to the following question: {question}",
        input_variables=["question"]
    )
    chain = LLMChain(llm=llm, prompt=prompt_template)
    return chain.run({"question": user_input})

# Function to generate and display a word cloud
def show_word_cloud(prompts):
    text = ' '.join(prompts)
    wordcloud = WordCloud(width=600, height=300, background_color='Black').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

# Dummy venue data
venue_data = {
    "Corporate": [
        {"name": "Venue A", "capacity": 100, "location": "Downtown"},
        {"name": "Venue B", "capacity": 50, "location": "Uptown"},
        {"name": "Venue C", "capacity": 150, "location": "City Center"},
    ],
    "Birthday": [
        {"name": "Birthday Venue A", "capacity": 30, "location": "Near Park"},
        {"name": "Birthday Venue B", "capacity": 20, "location": "Coastal Area"},
    ],
    "Wedding": [
        {"name": "Wedding Venue A", "capacity": 200, "location": "Beachside"},
        {"name": "Wedding Venue B", "capacity": 150, "location": "Garden"},
    ]
}

# Function to get venue suggestions based on event type and capacity
def get_venue_suggestions(event_type, capacity):
    suggestions = []
    for venue in venue_data.get(event_type, []):
        if venue["capacity"] >= capacity:
            suggestions.append(venue)
    return suggestions

# Function to generate a random color
def random_color():
    return f'#{random.randint(0, 0xFFFFFF):06x}'

# Custom CSS for the app
st.markdown("""
    <style>
    body {
        font-family: 'Helvetica', sans-serif;
        background-color: #f9f9f9;
    }
    .container {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin: 20px 0;
    }
    .custom-button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 15px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .custom-button:hover {
        background-color: #45a049;
    }
    .question {
        font-weight: bold;
        color: #333;
    }
    .response {
        background-color: #e7f3fe;
        border-left: 6px solid #2196F3;
        padding: 10px;
        margin-top: 5px;
    }
    .venue-card {
        background-color: #fff3e6;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
    }
    .venue-card:hover {
        transform: scale(1.02);
    }
    .venue-details {
        display: none;
    }
    .venue-card:hover .venue-details {
        display: block;
    }
    </style>
""", unsafe_allow_html=True)

# Main application function
def main():
    st.title("APCO Event Planning Assistant")
    st.markdown("---")

    # Sidebar with app description
    st.sidebar.title("About Application")
    st.sidebar.write("""
        This Event Planning Assistant helps you manage and organize various events seamlessly. 
        You can ask questions about event planning, view past interactions, generate word clouds 
        based on your queries, and get venue suggestions based on your requirements.
    """)

    # Input for OpenAI API key
    api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
    
    # Initialize session states for chat history and prompts
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'prompts' not in st.session_state:
        st.session_state.prompts = []

    # Create tabs for different functionalities
    tab1, tab2, tab3, tab4 = st.tabs(["Search and Check Results", "Chat History", "Word Cloud", "Venue Suggestions"])

    with tab1:
        st.header("Search and Check Results")
        # User input for questions
        user_input = st.text_input("Ask your event planning question:")
        
        if st.button("Submit", key="submit_btn"):
            if user_input:
                response = query_assistant(user_input, api_key)
                st.session_state.history.append((user_input, response))
                st.session_state.prompts.append(user_input)

        # Display the most recent result in a styled container
        if st.session_state.history:
            recent_question, recent_response = st.session_state.history[-1]
            with st.container():
                st.markdown("<div class='container'>", unsafe_allow_html=True)
                st.markdown("### Recent Result")
                st.markdown(f"<p class='question'>**You:** {recent_question}</p>", unsafe_allow_html=True)
                st.markdown(f"<div class='response'><strong>Assistant:</strong> {recent_response}</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.header("Chat History")
        # Expandable section for past interactions
        if st.session_state.history:
            with st.expander("View Past Interactions"):
                for user_question, assistant_response in st.session_state.history:
                    st.markdown(f"<p class='question'>**You:** {user_question}</p>", unsafe_allow_html=True)
                    # Apply random color for assistant's response
                    assistant_color = random_color()
                    st.markdown(f"<div class='response' style='border-left: 6px solid {assistant_color};'><strong>Assistant:</strong> {assistant_response}</div>", unsafe_allow_html=True)
        else:
            st.write("No chat history available.")

    with tab3:
        st.header("Word Cloud")
        # Generate and display word cloud
        if st.session_state.prompts:
            show_word_cloud(st.session_state.prompts)
        else:
            st.write("No prompts available for word cloud generation.")

    with tab4:
        st.header("Venue Suggestions")
        # Venue suggestions based on user input
        event_type = st.selectbox("Select event type:", ["Corporate", "Birthday", "Wedding"])
        capacity = st.number_input("Enter the number of guests:", min_value=1)
        if st.button("Get Venue Suggestions"):
            suggestions = get_venue_suggestions(event_type, capacity)
            if suggestions:
                st.write("### Venue Suggestions:")
                for venue in suggestions:
                    venue_color = random_color()  # Generate a random color for each venue card
                    st.markdown(f"""
                        <div class='venue-card' style='border-left: 6px solid {venue_color};'>
                            <h5>{venue['name']}</h5>
                            <p><strong>Capacity:</strong> {venue['capacity']}</p>
                            <p><strong>Location:</strong> {venue['location']}</p>
                            <div class='venue-details'>
                                <p>More details about the venue can be added here.</p>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.write("No suitable venues found.")

# Run the application
if __name__ == "__main__":
    main()
