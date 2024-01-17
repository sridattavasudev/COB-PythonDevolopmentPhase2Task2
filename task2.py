from wordcloud import WordCloud
import matplotlib.pyplot as plt

# task2


def generate_word_cloud(text):
    # Create a WordCloud object
    wordcloud = WordCloud(
        width=800,
        height=400,
        random_state=21,
        max_font_size=110,
        background_color="white",
    ).generate(text)

    # Display the generated word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


sample_text = input(str("Enter the text to generate cloud"))
# Generate word cloud from the sample text
generate_word_cloud(sample_text)
