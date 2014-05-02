import csv
import os
import pandas as pd
import ConfigParser
from dataset import get_Wrapper, get_Fields, get_Projects, get_Courses, get_CDT_Wrapper, create_child_template, getNameforId, get_Fields_Ids, get_No_FieldIds


config = ConfigParser.RawConfigParser()
config.read('sdf.cfg')

name_coll = ["Q3_1_TEXT", "Q3_2_TEXT","Q3_5_TEXT","Q3_3_TEXT","Q3_4_TEXT"]

project_title_coll = [["Q38_1_TEXT","Q38_4_TEXT","Q38_3_TEXT","Q38_5_TEXT","Q38_6_TEXT","Q40_1_TEXT"], 
["Q46_1_TEXT","Q46_4_TEXT","Q46_3_TEXT","Q46_5_TEXT","Q46_6_TEXT","Q48_1_TEXT"], ["Q54_1_TEXT","Q54_4_TEXT","Q54_3_TEXT","Q54_5_TEXT","Q54_6_TEXT","Q56_1_TEXT"],
["Q62_1_TEXT","Q62_4_TEXT","Q62_3_TEXT","Q62_5_TEXT","Q62_6_TEXT","Q64_1_TEXT"], ["Q70_1_TEXT","Q70_4_TEXT","Q70_3_TEXT","Q70_5_TEXT","Q70_6_TEXT","Q72_1_TEXT"]]

corse_title_coll = [["Q8_2_TEXT", "Q8_1_TEXT", "Q8_3_TEXT"], ["Q15_2_TEXT", "Q15_1_TEXT", "Q15_3_TEXT"], ["Q21_2_TEXT", "Q21_1_TEXT", "Q21_3_TEXT"], ["Q26_2_TEXT", "Q26_1_TEXT", "Q26_3_TEXT"], ["Q31_2_TEXT", "Q31_1_TEXT", "Q31_3_TEXT"]]


pplfocus = ["Q5_1","Q5_2","Q5_3","Q5_4","Q5_5","Q5_6","Q5_7","Q5_8","Q5_9"]
coursefocus = [["Q9_1","Q9_2","Q9_3","Q9_4","Q9_5","Q9_6","Q9_7","Q9_8","Q9_9"],["Q16_1","Q16_2","Q16_3","Q16_4","Q16_5",
"Q16_6","Q16_7","Q16_8","Q16_9"],["Q22_1","Q22_2","Q22_3","Q22_4","Q22_5","Q22_6","Q22_7","Q22_8","Q22_9"],["Q27_1","Q27_2",
"Q27_3","Q27_4","Q27_5","Q27_6","Q27_7","Q27_8","Q27_9"],["Q32_1","Q32_2","Q32_3","Q32_4","Q32_5","Q32_6","Q32_7","Q32_8",
"Q32_9"]]

projectfocus = [["Q43_1","Q43_2","Q43_3","Q43_4","Q43_5","Q43_6","Q43_7","Q43_8","Q43_9"],["Q51_1","Q51_2","Q51_3","Q51_4",
"Q51_5","Q51_6","Q51_7","Q51_8","Q51_9"],["Q59_1","Q59_2","Q59_3","Q59_4","Q59_5","Q59_6","Q59_7","Q59_8","Q59_9"],["Q67_1",
"Q67_2","Q67_3","Q67_4","Q67_5","Q67_6","Q67_7","Q67_8","Q67_9"],["Q75_1","Q75_2","Q75_3","Q75_4","Q75_5","Q75_6","Q75_7",
"Q75_8","Q75_9"]]

cdt_ppl = ["Q6_1","Q6_2","Q6_3","Q6_4","Q6_5","Q6_6","Q6_7","Q6_8"]
cdt_course = [["Q10_1","Q10_2","Q10_3","Q10_4","Q10_5","Q10_6","Q10_7","Q10_8","Q10_9"],["Q17_1","Q17_2","Q17_3","Q17_4","Q17_5","Q17_6","Q17_7","Q17_8","Q17_9"],
["Q23_1","Q23_2","Q23_3","Q23_4","Q23_5","Q23_6","Q23_7","Q23_8","Q23_9"],["Q28_1","Q28_2","Q28_3","Q28_4","Q28_5","Q28_6","Q28_7","Q28_8","Q28_9"],
["Q33_1","Q33_2","Q33_3","Q33_4","Q33_5","Q33_6","Q33_7","Q33_8","Q33_9"]]

cdt_project = [["Q44_1","Q44_2","Q44_3","Q44_4","Q44_5","Q44_6","Q44_7","Q44_8","Q44_9"],["Q52_1","Q52_2","Q52_3","Q52_4","Q52_5","Q52_6","Q52_7","Q52_8","Q52_9"],
["Q60_1","Q60_2","Q60_3","Q60_4","Q60_5","Q60_6","Q60_7","Q60_8","Q60_9"],["Q68_1","Q68_2","Q68_3","Q68_4","Q68_5","Q68_6","Q68_7","Q68_8","Q68_9"],
["Q76_1","Q76_2","Q76_3","Q76_4","Q76_5","Q76_6","Q76_7","Q76_8","Q76_9"]]

field_ids = ["F0","F1","F2","F3","F4","F5","F6","F7","F8","F9"]
cdt_ids = ["CDT0","CDT1","CDT2","CDT3","CDT4","CDT5","CDT6","CDT7","CDT8","CDT9"]

cross_ref_dict = {}
cross_ref_cdt = {}
cross_ref_size = {}
ultimate_cross_ref_dict = {}
ultimate_cross_ref_names = {}
ultimate_cross_ref_cdt= {}

dir = config.get('prod', 'sdf-data-path')


def initialize():
	cls()
	global CHART_DATA
	CHART_DATA = load_data_from_csv()
	global FIELDS_ARRAY
	FIELDS_ARRAY = get_Fields()
	global PROJECTS_ARRAY
	PROJECTS_ARRAY = get_Projects()
	global COURSES_ARRAY
	COURSES_ARRAY = get_Courses()
	global WRAPPER_DATA
	WRAPPER_DATA = get_Wrapper()
	global CDT_WRAPPER_DATA
	CDT_WRAPPER_DATA = get_CDT_Wrapper()


def load_data_from_csv():
    chart_data = pd.read_csv(dir + 'Seeding_Food_Studies_Main.csv', sep=',', index_col=None, header=0);
    return chart_data 


def getPeopleForField(fieldId):
	people_names = []
	col = FIELDS_ARRAY[fieldId]
	tmp = CHART_DATA.loc[1:,[name_coll[0],name_coll[1],cdt_ppl[0],cdt_ppl[1],cdt_ppl[2],cdt_ppl[3],cdt_ppl[4],cdt_ppl[5],
	cdt_ppl[6],cdt_ppl[7],name_coll[2],pplfocus[0],pplfocus[1],pplfocus[2],pplfocus[3],pplfocus[4],pplfocus[5],pplfocus[6],
	pplfocus[7],pplfocus[8],corse_title_coll[0][0],corse_title_coll[0][1],corse_title_coll[1][0],corse_title_coll[1][1],
	corse_title_coll[2][0],corse_title_coll[2][1],corse_title_coll[3][0],corse_title_coll[3][1],corse_title_coll[4][0],
	corse_title_coll[4][1],project_title_coll[0][0],project_title_coll[0][1],project_title_coll[1][0],project_title_coll[1][1],
	project_title_coll[2][0],project_title_coll[2][1],project_title_coll[3][0],project_title_coll[3][1],project_title_coll[4][0],
	project_title_coll[4][1],name_coll[3],name_coll[4]]]

	tmp = tmp.dropna(subset=[pplfocus[get_No_FieldIds(fieldId)],name_coll[0]])
	tmp = tmp.fillna("0");

	for row in tmp.itertuples():
		create_cross_ref_map([fieldId,fieldId+"_P1",fieldId+"_P1_I1"],row[1],cross_ref_dict)
		
		f = []
		for i in xrange(12,21):
			if row[i] == "1":
				f.append(getNameforId(get_Fields_Ids(str(i))))
		c = []

		for i in xrange(21,31,2):
			if row[i] != "0" :
				a = {
				"course_no" : row[i],
				"course_title" : row[i+1]
				}
				c.append(a)
				create_cross_ref_map(get_content_data(row[i]),row[1],ultimate_cross_ref_dict)
				create_cross_ref_map([row[i].lower()],row[1],ultimate_cross_ref_names)
		p = []
		
		for i in xrange(31,41,2):
			if row[i] != "0" :
				b = {
				"project_title" : row[i],
				"project_investigator" : row[i+1]
				}
				p.append(b)
				create_cross_ref_map(get_content_data(row[i]),row[1],ultimate_cross_ref_dict)
				create_cross_ref_map([row[i].lower()],row[1],ultimate_cross_ref_names)		

		t={
		#"parent_id" : fieldId+"_P1_I1",
		"i_type" : "people",
		"i_header_text" : row[1],
		"i_content_text" : row[2],
		"i_degree_text" : row[11],
		"i_focus" : f,
		"i_courses" : c,
		"i_projects" : p,
		"i_department": row[41],
		"i_college": row[42]
		}
		s = []
		for i in xrange(3,11):
			mystr = cdt_ids[(i-2)]+"_"+fieldId+"_P1"
			if row[i] == "1" :
				cross_ref_cdt[mystr] = 1
				s.append(mystr)
			else:
				if mystr not in cross_ref_cdt: 
					cross_ref_cdt[mystr] = 0
				
		cross_ref_cdt["CDT9"+"_"+fieldId+"_P1"] = 0			
		t['cdt'] = s
		people_names.append(t)

		cross_ref_size[fieldId+"_P1"] = len(people_names)
		create_cross_ref_map(s,row[1],ultimate_cross_ref_cdt)

	return people_names



def getCoursesForField(fieldId):
	course_names = []
	cols = COURSES_ARRAY[fieldId]
	for i in xrange(len(cols)):
		tmp = CHART_DATA.loc[1:,[corse_title_coll[i][0],corse_title_coll[i][1],cdt_course[i][0],
		cdt_course[i][1],cdt_course[i][2],cdt_course[i][3],cdt_course[i][4],cdt_course[i][5],
		cdt_course[i][6],cdt_course[i][7],cdt_course[i][8],coursefocus[i][0],coursefocus[i][1],coursefocus[i][2]
		,coursefocus[i][3],coursefocus[i][4],coursefocus[i][5],coursefocus[i][6],coursefocus[i][7],coursefocus[i][8]
		,corse_title_coll[i][2],"Q4_1","Q3_1_TEXT"]]
		tmp = tmp.dropna(subset=[coursefocus[i][get_No_FieldIds(fieldId)]])
		tmp = tmp.fillna("0");
		for row in tmp.itertuples():
			create_cross_ref_map([fieldId,fieldId+"_C1",fieldId+"_C1_I1"],row[1],cross_ref_dict)
			
			f = []
			for j in xrange(12,21):
				if row[j] == "1":
					f.append(getNameforId(get_Fields_Ids(str(j))))

			prof = ""
			if row[22] == "1":
				prof = row[23]
				create_cross_ref_map(get_content_data(row[23]),row[1],ultimate_cross_ref_dict)
				create_cross_ref_map([row[23].lower()],row[1],ultimate_cross_ref_names)

			t = {
			#"parent_id" : fieldId+"_C1_I1",
			"i_type" : "courses",
			"i_header_text" : row[1],
			"i_content_text" : row[2],
			"i_keywords" : row[21],
			"i_professor": prof,
			"i_focus" : f
			}
			s = []
			for i in range(3,12):
				mystr = cdt_ids[(i-2)]+"_"+fieldId+"_C1"
				if row[i] == "1" :
					cross_ref_cdt[mystr] = 1
					s.append(mystr)
				else:
					if mystr not in cross_ref_cdt: 
						cross_ref_cdt[mystr] = 0

			t['cdt'] = s
			course_names.append(t)

			cross_ref_size[fieldId+"_C1"] = len(course_names)
			create_cross_ref_map(s,row[1],ultimate_cross_ref_cdt)
	return course_names


def getProjectsForField(fieldId):
	project_names = []
	cols = PROJECTS_ARRAY[fieldId]
	for i in xrange(len(cols)):
		tmp = CHART_DATA.loc[1:,[project_title_coll[i][0],project_title_coll[i][1],cdt_project[i][0],cdt_project[i][1],
		cdt_project[i][2],cdt_project[i][3],cdt_project[i][4],cdt_project[i][5],cdt_project[i][6],cdt_project[i][7],
		cdt_project[i][8],projectfocus[i][0],projectfocus[i][1],projectfocus[i][2],projectfocus[i][3],projectfocus[i][4],
		projectfocus[i][5],projectfocus[i][6],projectfocus[i][7],projectfocus[i][8],project_title_coll[i][2],project_title_coll[i][3],
		project_title_coll[i][4],project_title_coll[i][5]]]
		tmp = tmp.dropna(subset=[project_title_coll[i][0],projectfocus[i][get_No_FieldIds(fieldId)]])
		tmp = tmp.fillna("0");
		for row in tmp.itertuples():
			create_cross_ref_map([fieldId,fieldId+"_R1",fieldId+"_R1_I1"],row[1],cross_ref_dict)

			f = []
			for j in xrange(12,21):
				if row[j] == "1":
					f.append(getNameforId(get_Fields_Ids(str(j))))

			create_cross_ref_map(get_content_data(row[2]),row[1],ultimate_cross_ref_dict)
			create_cross_ref_map(get_content_data(row[24]),row[1],ultimate_cross_ref_dict)
			create_cross_ref_map([row[2].lower(),row[24].lower()],row[1],ultimate_cross_ref_names)

			t={
			#"parent_id" : fieldId+"_R1_I1",
			"i_type" : "projects",
			"i_header_text" : row[1],
			"i_content_text" : row[2],
			"i_website" : row[21],
			"i_ncsu_team" : row[24],
			"i_start_date" : row[22],
			"i_end_date" : row[23],
			"i_focus" : f
			}
			s = []
			for i in xrange(3,12):
				mystr = cdt_ids[(i-2)]+"_"+fieldId+"_R1"
				if row[i] == "1" :
					cross_ref_cdt[mystr] = 1
					s.append(mystr)
				else:
					if mystr not in cross_ref_cdt: 
						cross_ref_cdt[mystr] = 0

			t['cdt'] = s
			project_names.append(t)

			cross_ref_size[fieldId+"_R1"] = len(project_names)
			create_cross_ref_map(s,row[1],ultimate_cross_ref_cdt)
	return project_names


def get_chart_data():
	chartObject = WRAPPER_DATA
	wrap = chartObject["children"];
	for field in wrap:

		child = field["children"]
		child[0]["children"][0]["content"] = sorted(getPeopleForField(field["id"]),key=lambda k: k['i_header_text'])
		s = len(child[0]["children"][0]["content"])
		child[0]["children"][0]["size"] = s
		child[0]["header_text"] = getNameforId(field["id"])
		child[0]["mid_text"] = "People"
		child[0]["content_text"] = "This survey uncovered "+str(s)+" people whose work relates to "+getNameforId(field["id"])
		child[0]["children"][0]["header_text"] = getNameforId(field["id"])
		child[0]["children"][0]["mid_text"] = "People"
		child[0]["children"][0]["content_text"] = "This survey uncovered "+str(s)+" people whose work relates to "+getNameforId(field["id"])

		child[1]["children"][0]["content"] = sorted(getCoursesForField(field["id"]),key=lambda k: k['i_header_text'])
		s = len(child[1]["children"][0]["content"])
		child[1]["children"][0]["size"] = s
		child[1]["header_text"] = getNameforId(field["id"])
		child[1]["mid_text"] = "Courses"
		child[1]["content_text"] = "This survey uncovered "+str(s)+" courses exploring "+getNameforId(field["id"])
		child[1]["children"][0]["header_text"] = getNameforId(field["id"])
		child[1]["children"][0]["mid_text"] = "Courses"
		child[1]["children"][0]["content_text"] = "This survey uncovered "+str(s)+" courses exploring "+getNameforId(field["id"])

		child[2]["children"][0]["content"] = sorted(getProjectsForField(field["id"]),key=lambda k: k['i_header_text'])
		s = len(child[2]["children"][0]["content"])
		child[2]["children"][0]["size"] = s
		child[2]["header_text"] = getNameforId(field["id"])
		child[2]["mid_text"] = "Projects"
		child[2]["content_text"] = "This survey uncovered "+str(s)+" current or recent projects researching "+getNameforId(field["id"])
		child[2]["children"][0]["header_text"] = getNameforId(field["id"])
		child[2]["children"][0]["mid_text"] = "Projects"
		child[2]["children"][0]["content_text"] = "This survey uncovered "+str(s)+" current or recent projects researching "+getNameforId(field["id"])

	return chartObject


def create_cross_ref_map(nl,ht,dictionary):
	ht = ht.lower()
	if ht in dictionary:
		dictionary[ht] = list(set(dictionary[ht]+nl))
	else:
		dictionary[ht] = nl


def get_content_data(ht):
	contentArray = []
	ht = ht.lower()
	if cross_ref_dict.has_key(ht):
		contentArray = cross_ref_dict[ht]
	
	return contentArray



def get_crossref_data_chart(ht):
	contentArray = []
	nameArray = []
	cdtArray = []
	ht = ht.lower()
 
	if cross_ref_dict.has_key(ht):
		contentArray = cross_ref_dict[ht]
	
	if ultimate_cross_ref_dict.has_key(ht):
		contentArray = list(set(contentArray+ultimate_cross_ref_dict[ht]))

	if ultimate_cross_ref_names.has_key(ht):
		nameArray = ultimate_cross_ref_names[ht]

	for name in nameArray:
		if ultimate_cross_ref_cdt.has_key(name):
			cdtArray = list(set(cdtArray+ultimate_cross_ref_cdt[name]))
		
	cdtArray = list(set(cdtArray+ultimate_cross_ref_cdt[ht]))

	obj = {
        "data" : contentArray,
        "cdt" : cdtArray
    }
    

	return obj


def get_content_data_chart(ht):
	contentArray = []
	ht = ht.lower()
	if cross_ref_dict.has_key(ht):
		contentArray = cross_ref_dict[ht]
	
	return contentArray



def get_cdt_data():
	cdtObject = CDT_WRAPPER_DATA
	cdt_wrap = cdtObject["children"]
	count = 0
	for field in cdt_wrap:
		count+=1
		child = field["children"]
		child[0]["children"] = create_cdt_data(field_ids[count]+"_P1")
		child[1]["children"] = create_cdt_data(field_ids[count]+"_C1")
		child[2]["children"] = create_cdt_data(field_ids[count]+"_R1")
	
	return cdtObject


def create_cdt_data(suffix):
	tmp = obj = create_child_template()
	
	for i in range(1,10):
		t = tmp
		myId = cdt_ids[i]+"_"+suffix
		t['id'] = myId
		t['visible'] = cross_ref_cdt[myId]
		if i == 9 : 
			t['size'] = cross_ref_size[suffix]
		
		if i < 9:	
			tmp = tmp['children'][0]
	
	return [obj]	

def cls():
    os.system(['clear','cls'][os.name == 'nt'])