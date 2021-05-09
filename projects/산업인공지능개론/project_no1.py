from durable.lang import *

with ruleset('company'):
    @when_all((m.predicate == '컨트롤러') & (m.object == '수정'))
    def color(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '색변환값', 'object': '수정필요' })

    @when_all((m.predicate == '리플렉터') & (m.object == '재설계'))
    def light(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '빛', 'object': '퍼짐' })

    @when_all(c.first << (m.predicate == '컨트롤러') & (m.object == '수정'), (m.predicate == '리플렉터') & (m.object == '재설계') & (m.subject == c.first.subject))
    def led(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': '구형 LED 모듈에 맞게', 'object': '설계됨' })    

    @when_all((m.predicate == '디자인') & (m.object == '재설계'))
    def design(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '외형', 'object': '투박함' })

    @when_all((m.predicate == 'Line레이저 길이') & (m.object == '조절'))
    def distance(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': 'Line레이저 길이', 'object': '거리에 따라 길어짐' })
        
    @when_all((m.predicate == 'Line레이저 길이') & (m.object == '거리에 따라 길어짐'))
    def angle(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': 'Line레이저 길이', 'object': '쏘는 각도에 따라 길어짐' })

    @when_all((m.predicate == '안테나위치') & (m.object == '수정'))
    def signal(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '전파강도', 'object': '개선필요' })

    @when_all((m.predicate == '전파강도') & (m.object == '개선필요'))
    def sw(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': 'S/W', 'object': '수정' })

    @when_all((m.predicate == '리시버') & (m.object == '사이즈수정'))
    def receiver(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': '리시버', 'object': '폭 큼' })

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))

assert_fact('company', { 'subject': '무영등', 'predicate': '컨트롤러', 'object': '수정' })
assert_fact('company', { 'subject': '무영등', 'predicate': '리플렉터', 'object': '재설계' })
assert_fact('company', { 'subject': '무영등', 'predicate': '디자인', 'object': '재설계' })
assert_fact('company', { 'subject': '레이저프리젠터', 'predicate': 'Line레이저 길이', 'object': '조절' })
assert_fact('company', { 'subject': '레이저프리젠터', 'predicate': '안테나위치', 'object': '수정' })
assert_fact('company', { 'subject': '레이저프리젠터', 'predicate': '리시버', 'object': '사이즈수정' })