from banks import Prompt

p = Prompt("Write a 500-word blog post on {{ topic }}.\n\nBlog post:")
topic = "retrogame computing"
print(p.text({"topic": topic}))
