from BeautifulSoup import Filter


#test sprawdzający czy w artykule pod linkiem występują 3 słowa kluczowe
abstract = 'AbstractTramadol/paracetamol 37.5mg/325mg (Tramacet®, Zaldiar®, Ixprim®, Kolibri®) is an orally administered fixed-dose combination of the atypical opioid tramadol and paracetamol, which is indicated in the EU for the symptomatic treatment of moderate to severe pain. This article reviews the pharmacological properties, clinical efficacy and tolerability of tramadol/paracetamol in adults with moderate to severe pain.Fixed-dose tramadol/paracetamol is a rapidly-acting, longer-duration, multi-modal analgesic, which is effective and generally well tolerated in patients with moderate to severe pain. In several well designed, clinical studies, single- or multiple-dose tramadol/paracetamol was effective in providing pain relief in adult patients with postoperative pain after minor surgery, musculoskeletal pain (acute, subacute or chronic), painful diabetic peripheral neuropathy or migraine pain. It was also effective as an add-on analgesic in patients who were experiencing moderate to severe musculoskeletal pain (e.g. osteoarthritis or rheumatoid arthritis pain) despite ongoing NSAID and/or disease-modifying antirheumatic drug therapy. Moreover, in patients with postoperative pain, ankle sprain pain or subacute lower back pain, the analgesic efficacy of tramadol/paracetamol was better than that of paracetamol, generally similar to, or better than that, of tramadol, and generally similar to that of ibuprofen or the fixed-dose combinations hydrocodone/paracetamol, codeine/paracetamol and codeine/paracetamol/ibuprofen. In addition, the analgesic efficacy of tramadol/paracetamol did not differ significantly from that of gabapentin in patients with chronic pain associated with diabetic peripheral neuropathy. Tramadol/paracetamol had no additional tolerability issues relative to its components and, overall, the tolerability profile of tramadol/paracetamol was generally similar to that of other active comparators (fixed-dose combinations or single-agents); however, incidences of some adverse events were lower in tramadol/paracetamol than in active comparator recipients. Although additional comparative and long-term studies would help to definitively position tramadol/paracetamol with respect to other analgesics, available clinical data suggest that tramadol/paracetamol is a useful treatment option for providing multimodal analgesia in patients with moderate to severe pain.'
set_of_sentence = set(((('AbstractTramadol/paracetamol 37.5mg/325mg (Tramacet®, Zaldiar®, Ixprim®, Kolibri®) is an orally administered fixed-dose combination of the atypical opioid tramadol and paracetamol, which is indicated in the EU for the symptomatic treatment of moderate to severe pain.').replace(',',' ')).replace('/',' ')).split(" "))


def test_create_set_of_abstract_words():
    filter = Filter('url1')
    filter.abstract = abstract
    filter.create_set_of_abstract_words()
    assert {'pain'}.issubset(filter.set_of_abstract_words) == True
    assert {'tramadol'}.issubset(filter.set_of_abstract_words) == True
    assert {'paracetamol'}.issubset(filter.set_of_abstract_words) == True

def test_create_list_of_sets_of_sentence():
    filter = Filter('url1')
    filter.abstract = abstract
    filter.create_list_of_sets_of_sentence()
    print(filter.list_abstract_sentence)
    assert set_of_sentence.issubset(set(filter.list_abstract_sentence)) == True


