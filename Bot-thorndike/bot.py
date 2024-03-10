from flask import Flask, request, jsonify

app = Flask(__name__)
# Lista de mensajes predeterminados

def presentation():
    message = "¡Hola! Me llamo Thorndike, ¡soy un asistente virtual! En mi versión 1, estoy aquí para proporcionarte información sobre Santiago Delebecq. Puedo ayudarte tanto con información personal (edad, fecha de nacimiento, etc.) como contarte sobre su educación."
    return message
def about(topic):
    topics = {
        "age": "Santi tiene 22 años de edad",
        "date_of_birth": "Santi nació el 21 de mayo del 2001",
        "place_of_birth": "Santi nació en El Maitén, en la provincia de Chubut, Argentina",
        "current_location": "Actualmente, Santi reside en la ciudad de Córdoba, en la provincia de Córdoba, Argentina"
    }
    return topics.get(topic, "Tema no encontrado")

def education(topic):
    topics = {
        "university": "La trayectoria universitaria de Santi comenzó con Ingeniería en Computación en la Facultad de Ciencias Exactas de la UNC. Sin embargo, decidió abandonar antes de completar el primer año para emprender un camino autodidacta en programación.",
        "henry": "El tiempo de Santi en Henry fue increíblemente enriquecedor. A través de esa experiencia, pudo sumergirse en el mundo de la programación, fortalecer sus habilidades técnicas y blandas, trabajar en proyectos reales y conectarse con una comunidad apasionada. Fue un período de intenso aprendizaje y crecimiento personal.",
        "autodidact": "Durante los últimos dos años, Santi ha estado inmerso en el aprendizaje autodidacta de programación. Comenzó explorando los fundamentos con JavaScript y luego se adentró en el desarrollo frontend, profundizando sus conocimientos en tecnologías como HTML, CSS y JavaScript. Actualmente, se considera un desarrollador versátil, capaz de trabajar en diferentes áreas, desde frontend hasta backend y full-stack. Siempre está buscando estar al día con las últimas tecnologías y está emocionado por explorar nuevas áreas como el machine learning y el desarrollo de aplicaciones móviles.",
        "lawyer": "Además de su pasión por la tecnología, Santi también está dedicando tiempo a estudiar Derecho en la Facultad de Derecho de la UNC, donde se encuentra en su primer año de carrera."
    }
    return topics.get(topic, "Tema no encontrado")

def option(case, topic=None):
    options = {
        "about": about,
        "education": education
    }
    selected_case = options.get(case)
    if selected_case:
        return selected_case(topic)
    else:
        return "No valido"
# ROUTINGS

#PRESENTACION
@app.route('/presentation', methods=['GET'])
def get_presentation():
       return jsonify(presentation())
#ABOUT
@app.route('/about/<topic>',methods=['GET'])
def get_about(topic):
    return jsonify(option("about", topic))
#EDUCATION
@app.route('/education/<topic>' ,methods=['GET'])
def get_education(topic):
    return jsonify(option("education", topic))
# Mostrar todas las opciones disponibles
@app.route('/options', methods=['GET'])
def get_options():
  return jsonify({
        "options": ["about", "education"]
    })
    

if __name__ == '__main__':
    app.run(debug=True)