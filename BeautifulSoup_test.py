from BeautifulSoup import Filter
import re

# test sprawdzający czy w artykule pod linkiem występują 3 słowa kluczowe
abstract = 'AbstractTramadol/paracetamol 37.5mg/325mg (Tramacet®, Zaldiar®, Ixprim®, Kolibri®) is an orally administered fixed-dose combination of the atypical opioid tramadol and paracetamol, which is indicated in the EU for the symptomatic treatment of moderate to severe pain. This article reviews the pharmacological properties, clinical efficacy and tolerability of tramadol/paracetamol in adults with moderate to severe pain.Fixed-dose tramadol/paracetamol is a rapidly-acting, longer-duration, multi-modal analgesic, which is effective and generally well tolerated in patients with moderate to severe pain. In several well designed, clinical studies, single- or multiple-dose tramadol/paracetamol was effective in providing pain relief in adult patients with postoperative pain after minor surgery, musculoskeletal pain (acute, subacute or chronic), painful diabetic peripheral neuropathy or migraine pain. It was also effective as an add-on analgesic in patients who were experiencing moderate to severe musculoskeletal pain (e.g. osteoarthritis or rheumatoid arthritis pain) despite ongoing NSAID and/or disease-modifying antirheumatic drug therapy. Moreover, in patients with postoperative pain, ankle sprain pain or subacute lower back pain, the analgesic efficacy of tramadol/paracetamol was better than that of paracetamol, generally similar to, or better than that, of tramadol, and generally similar to that of ibuprofen or the fixed-dose combinations hydrocodone/paracetamol, codeine/paracetamol and codeine/paracetamol/ibuprofen. In addition, the analgesic efficacy of tramadol/paracetamol did not differ significantly from that of gabapentin in patients with chronic pain associated with diabetic peripheral neuropathy. Tramadol/paracetamol had no additional tolerability issues relative to its components and, overall, the tolerability profile of tramadol/paracetamol was generally similar to that of other active comparators (fixed-dose combinations or single-agents); however, incidences of some adverse events were lower in tramadol/paracetamol than in active comparator recipients. Although additional comparative and long-term studies would help to definitively position tramadol/paracetamol with respect to other analgesics, available clinical data suggest that tramadol/paracetamol is a useful treatment option for providing multimodal analgesia in patients with moderate to severe pain.'
set_of_sentence1 = set(re.sub(r"[^a-zA-Z]", " ", 'AbstractTramadol/paracetamol 37.5mg/325mg (Tramacet®, Zaldiar®, Ixprim®, Kolibri®) is an orally administered fixed-dose combination of the atypical opioid tramadol and paracetamol, which is indicated in the EU for the symptomatic treatment of moderate to severe pain.').split(" "))
set_of_sentence2 = set(re.sub(r"[^a-zA-Z]", " ", 'Fixed-dose tramadol/paracetamol is a rapidly-acting, longer-duration, multi-modal analgesic, which is effective and generally well tolerated in patients with moderate to severe pain.').split(" "))
set_of_sentence3 = set(re.sub(r"[^a-zA-Z]", " ", 'In several well designed, clinical studies, single- or multiple-dose tramadol/paracetamol was effective in providing pain relief in adult patients with postoperative pain after minor surgery, musculoskeletal pain (acute, subacute or chronic), painful diabetic peripheral neuropathy or migraine pain.').split(" "))


def test_create_set_of_abstract_words():
    filter = Filter('url1')
    filter.abstract = abstract
    filter.create_set_of_abstract_words()
    assert {'pain'}.issubset(filter.set_of_abstract_words) == True
    assert {'tramadol'}.issubset(filter.set_of_abstract_words) == True
    assert {'paracetamol'}.issubset(filter.set_of_abstract_words) == True


def test_create_list_of_sets_of_sentence():
    filter = Filter('url1')
    filter.abstract = abstract                                                          # dopisujemy do 2-go pola obiektu nasz abstract
    filter.create_list_of_sets_of_sentence()                                            # dopisujemy do 3-go pola obiektu listę zdań w abstrakcie
    assert set_of_sentence1.issubset(filter.list_of_abstract_sentence_sets[0]) == True  # porównujemy czy pierwsze zdanie - set_of_sentence1 - wystepuje w liście zdań w abstract z pliku BeautifulSoup.py
    assert set_of_sentence2.issubset(filter.list_of_abstract_sentence_sets[1]) == True  # porównujemy czy drugie zdanie [1], tj. set_of_sentence2 - wystepuje w liście zdań w abstract z pliku BeautifulSoup.py
    assert set_of_sentence3.issubset(filter.list_of_abstract_sentence_sets[2]) == True  # porównujemy czy drugie zdanie [2], tj. set_of_sentence3 - wystepuje w liście zdań w abstract z pliku BeautifulSoup.py


def test_check_abstract():
    filter = Filter('url1')
    filter.abstract = abstract
    filter.create_set_of_abstract_words()
    assert {'pain', 'tramadol', 'paracetamol'}.issubset(filter.set_of_abstract_words) == True          # sprawdzamy czy w abstract występują wszystkie 3 podane słowa - test będzie zdany dla warunku True
    assert {'clinical', 'painful', 'neuropathy'}.issubset(filter.set_of_abstract_words) == True        # sprawdzamy czy w abstract występują wszystkie 3 podane słowa - test będzie zdany dla warunku True
    assert {'tolerability', 'chronic', 'symptomatic'}.issubset(filter.set_of_abstract_words) == True   # sprawdzamy czy w abstract występują wszystkie 3 podane słowa - test będzie zdany dla warunku True
    assert {'znieczulenie', 'gabapentin', 'treatment'}.issubset(filter.set_of_abstract_words) == False # sprawdzamy czy jak w abstract występują 2 słowa a jedno nie, to czy wynik wyświetli się zdany dla warunku False. Jeśli tak, to dobrze, gdyż muszą wystąpić wszystkie 3 słowa jednocześnie w całym abstract aby test był zdanny - warunek False dla 2 słow w tekście jest zatem prawdziwy.


def test_check_abstract_sentences():
    filter = Filter('url1')
    filter.abstract = abstract
    filter.create_list_of_sets_of_sentence()
    assert {'pain', 'tramadol', 'paracetamol'}.issubset(filter.list_of_abstract_sentence_sets[0]) == True   # sprawdzamy czy w pierwszym zdaniu - set_of_sentence1 [0], występują wszystkie 3 podane słowa - test będzie zdany dla warunku True
    assert {'pain', 'tramadol', 'paracetamol'}.issubset(filter.list_of_abstract_sentence_sets[1]) == True   # sprawdzamy czy w pierwszym zdaniu - set_of_sentence2 [1], występują wszystkie 3 podane słowa - test będzie zdany dla warunku True
    assert {'pain', 'tramadol', 'paracetamol'}.issubset(filter.list_of_abstract_sentence_sets[2]) == True   # sprawdzamy czy w pierwszym zdaniu - set_of_sentence3 [2], występują wszystkie 3 podane słowa - test będzie zdany dla warunku True
    assert {'pain', 'tramadol', 'znieczulenie'}.issubset(filter.list_of_abstract_sentence_sets[2]) == False # sprawdzamy czy jak w w zdaniu - set_of_sentence3 [2], występują 2 słowa a jedno nie, to czy wynik wyświetli się zdany dla warunku False. Jeśli tak, to dobrze, gdyż muszą wystąpić wszystkie 3 słowa jednocześnie w całym zdaniu aby test był zdanny - warunek False dla 2 słow w tekście jest zatem prawdziwy.
