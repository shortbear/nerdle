import pandas as pd
import streamlit as st

HEADER_GREEN = '% Chance of green letter(s)'
HEADER_GREEN_YELLOW = '% Chance of green/yellow letter(s)'
HEADER_DUPLICATES = 'Has duplicate letters'

@st.cache
def load_probs():
  df = pd.read_csv('./data/probs.csv')
  new_cols = {
    'word': 'Word',
    'probability_of_correct_position': HEADER_GREEN,
    'probability_of_match': HEADER_GREEN_YELLOW,
    'duplicate_letters': HEADER_DUPLICATES
  }
  df.rename(columns=new_cols, inplace=True)
  return df

def sorted_head(df, cols, ascending=[False, False]):
  return df.sort_values(cols, ascending=ascending).head().reset_index(drop=True).drop(columns=[HEADER_DUPLICATES])

df = load_probs()

st.title('Project Nerdle')
st.write('Enter your favorite starting word for [Wordle](https://www.nytimes.com/games/wordle/index.html), and see your chances of getting a green or yellow letter.')

with st.form('word_search'):
  word = st.text_input('Favorite starter word')
  submitted = st.form_submit_button("Submit")

  if submitted:
    if len(word) != 5:
      st.write('Wordle words must be 5 letters.')
    else:
      res = df.loc[df['Word'] == word.lower()]
      if res.shape[0] == 1:
        p_green = str(round(res[HEADER_GREEN].values[0] * 100, 2))
        p_green_yellow = str(round(res[HEADER_GREEN_YELLOW].values[0] * 100, 2))

        st.header(f'Probabilities for _{word}_:')
        col1, col2 = st.columns(2)
        with col1:
          st.metric('Green Letter(s)', value=f'{p_green}%')
        with col2:
          st.metric('Green/Yellow Letter(s)', value=f'{p_green_yellow}%')

      else:
        st.write('No match found')

st.caption('For methodology, visit [Kaggle](https://www.kaggle.com/shortbear/finding-the-best-starter-word-for-wordle).')

st.header('Need a better word?')
st.write("Here are the best starting words, depending on your priorities.")

st.subheader('Green letter(s) (w/o duplicates)')
st.table(data=sorted_head(df[~df[HEADER_DUPLICATES]], [HEADER_GREEN, HEADER_GREEN_YELLOW]))

st.subheader('Green letter(s) (with duplicates)')
st.table(data=sorted_head(df, [HEADER_GREEN, HEADER_GREEN_YELLOW]))

st.subheader('Green or yellow letter(s)')
st.table(data=sorted_head(df, [HEADER_GREEN_YELLOW, HEADER_GREEN]))

st.header('Need a terrible word?')
st.write("Here are the worst options.")

st.subheader('Green letter(s)')
st.table(data=sorted_head(df, [HEADER_GREEN, HEADER_GREEN_YELLOW], [True, True]))

st.subheader('Green or yellow letter(s)')
st.table(data=sorted_head(df, [HEADER_GREEN_YELLOW, HEADER_GREEN], [True, True]))