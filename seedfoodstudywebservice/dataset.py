

def get_Projects():
    projects = {
    "F1" : ["Q43_1", "Q51_1", "Q59_1", "Q67_1", "Q75_1"],
    "F2" : ["Q43_2", "Q51_2", "Q59_2", "Q67_2", "Q75_2"],
    "F3" : ["Q43_3", "Q51_3", "Q59_3", "Q67_3", "Q75_3"],
    "F4" : ["Q43_4", "Q51_4", "Q59_4", "Q67_4", "Q75_4"],
    "F5" : ["Q43_5", "Q51_5", "Q59_5", "Q67_5", "Q75_5"],
    "F6" : ["Q43_6", "Q51_6", "Q59_6", "Q67_6", "Q75_6"],
    "F7" : ["Q43_7", "Q51_7", "Q59_7", "Q67_7", "Q75_7"],
    "F8" : ["Q43_8", "Q51_8", "Q59_8", "Q67_8", "Q75_8"],
    "F9" : ["Q43_9", "Q51_9", "Q59_9", "Q67_9", "Q75_9"]
    }
    return projects


def get_Courses():
    courses = {
    "F1" : ["Q9_1", "Q16_1", "Q22_1", "Q27_1", "Q32_1"],
    "F2" : ["Q9_2", "Q16_2", "Q22_2", "Q27_2", "Q32_2"],
    "F3" : ["Q9_3", "Q16_3", "Q22_3", "Q27_3", "Q32_3"],
    "F4" : ["Q9_4", "Q16_4", "Q22_4", "Q27_4", "Q32_4"],
    "F5" : ["Q9_5", "Q16_5", "Q22_5", "Q27_5", "Q32_5"],
    "F6" : ["Q9_6", "Q16_6", "Q22_6", "Q27_6", "Q32_6"],
    "F7" : ["Q9_7", "Q16_7", "Q22_7", "Q27_7", "Q32_7"],
    "F8" : ["Q9_8", "Q16_8", "Q22_8", "Q27_8", "Q32_8"],
    "F9" : ["Q9_9", "Q16_9", "Q22_9", "Q27_9", "Q32_9"]
    }
    return courses


def get_Fields():
    fields = {
    "F1" : "Q5_1",
    "F2" : "Q5_2",
    "F3" : "Q5_3",
    "F4" : "Q5_4",
    "F5" : "Q5_5",
    "F6" : "Q5_6",
    "F7" : "Q5_7",
    "F8" : "Q5_8",
    "F9" : "Q5_9"
    }
    return fields

def get_cross_disp_courses():
    project_cdt = {
    "CDT1" : ["Q44_1", "Q52_1", "Q60_1", "Q68_1", "Q76_1"],
    "CDT2" : ["Q44_2", "Q52_2", "Q60_2", "Q68_2", "Q76_2"],
    "CDT3" : ["Q44_3", "Q52_3", "Q60_3", "Q68_3", "Q76_3"],
    "CDT4" : ["Q44_4", "Q52_4", "Q60_4", "Q68_4", "Q76_4"],
    "CDT5" : ["Q44_5", "Q52_5", "Q60_5", "Q68_5", "Q76_5"],
    "CDT6" : ["Q44_6", "Q52_6", "Q60_6", "Q68_6", "Q76_6"],
    "CDT7" : ["Q44_7", "Q52_7", "Q60_7", "Q68_7", "Q76_7"],
    "CDT8" : ["Q44_8", "Q52_8", "Q60_8", "Q68_8", "Q76_8"],
    "CDT9" : ["Q44_9", "Q52_9", "Q60_9", "Q68_9", "Q76_9"]
    }
    return project_cdt


def get_cross_disp_courses():
    course_cdt = {
    "CDT1" : ["Q10_1","Q17_1","Q23_1","Q28_1","Q33_1"],
    "CDT2" : ["Q10_2","Q17_2","Q23_2","Q28_2","Q33_2"],
    "CDT3" : ["Q10_3","Q17_3","Q23_3","Q28_3","Q33_3"],
    "CDT4" : ["Q10_4","Q17_4","Q23_4","Q28_4","Q33_4"],
    "CDT5" : ["Q10_5","Q17_5","Q23_5","Q28_5","Q33_5"],
    "CDT6" : ["Q10_6","Q17_6","Q23_6","Q28_6","Q33_6"],
    "CDT7" : ["Q10_7","Q17_7","Q23_7","Q28_7","Q33_7"],
    "CDT8" : ["Q10_8","Q17_8","Q23_8","Q28_8","Q33_8"],
    "CDT9" : ["Q10_9","Q17_9","Q23_9","Q28_9","Q33_9"]
    }
    return course_cdt


def get_cross_disp_people():
    people_cdt = {
    "CDT1" : "Q6_1",
    "CDT2" : "Q6_2",
    "CDT3" : "Q6_3",
    "CDT4" : "Q6_4",
    "CDT5" : "Q6_5",
    "CDT6" : "Q6_6",
    "CDT7" : "Q6_7",
    "CDT8" : "Q6_8",
    }
    return people_cdt


def get_cross_disciplinary_themes():
    cdt = {
    "CDT1" : "SOCIAL EQUITY",
    "CDT2" : "PUBLIC POLICY",
    "CDT3" : "FOOD ACCESS",
    "CDT4" : "CULTURAL HERITAGE",
    "CDT5" : "HEALTH NUTRITION",
    "CDT6" : "SUSTAINABILITY",
    "CDT7" : "ENVIORNMENTAL IMPACTS",
    "CDT8" : "ECONOMIC DEVELOPMENT",
    "CDT9" : "EDUCTAION"
    }
    return cdt

def getNameforId(Id):
    return{
    "F1" : "LAND USE PLANNING",
    "F2" : "SUITABILITY & SOIL SCIENCE",
    "F3" : "PRODUCTION & HARVESTING",
    "F4" : "TRANSPORTATION & DISTRIBUTION",
    "F5" : "AGGREGATION",
    "F6" : "PROCESSING & MANUFACTURING",
    "F7" : "MARKETING & RETAIL",
    "F8" : "CONSUMPTION",
    "F9" : "RESOURCE & WASTE RECOVERY"
    }[Id]

def get_Fields_Ids(x):
    return{
    "12" : "F1",
    "13" : "F2",
    "14" : "F3",
    "15" : "F4",
    "16" : "F5",
    "17" : "F6",
    "18" : "F7",
    "19" : "F8",
    "20" : "F9"
    }[x]
    
def get_No_FieldIds(x):
    return{
    "F1" : 0,
    "F2" : 1,
    "F3" : 2,
    "F4" : 3,
    "F5" : 4,
    "F6" : 5,
    "F7" : 6,
    "F8" : 7,
    "F9" : 8
    }[x]



def get_CDT_Wrapper():
    CDT_Wrapper = {
    "name" : "Cross Disciplinary Themes",
    "id" : "CDT0",
    "visible" : 0,
    "children" : [
    {
        "id" : "CDT_F1",
        "name" : "F1",
        "visible" : 0,
        "children" :[
        {
            "id" : "CDT_F1_P1",
            "name" : "F1",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F1_C1",
            "name" : "F1",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F1_R1",
            "name" : "F1",
            "visible" : 0,
            "children" : []
        }
        ]
    },
    {
        "id" : "CDT_F2",
        "name" : "F2",
        "visible" : 0,
        "children" :[
        {
            "id" : "CDT_F2_P1",
            "name" : "F2",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F2_C1",
            "name" : "F2",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F2_R1",
            "name" : "F2",
            "visible" : 0,
            "children" : []
        }
        ]
    },
    {
        "id" : "CDT_F3",
        "name" : "F3",
        "visible" : 0,
        "children" :[
        {
            "id" : "CDT_F3_P1",
            "name" : "F3",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F3_C1",
            "name" : "F3",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F3_R1",
            "name" : "F3",
            "visible" : 0,
            "children" : []
        }
        ]
    },
    {
        "id" : "CDT_F4",
        "name" : "F4",
        "visible" : 0,
        "children" :[
        {
            "id" : "CDT_F4_P1",
            "name" : "F4",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F4_C1",
            "name" : "F4",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F4_R1",
            "name" : "F4",
            "visible" : 0,
            "children" : []
        }
        ]
    },
    {
        "id" : "CDT_F5",
        "name" : "F5",
        "visible" : 0,
        "children" :[
        {
            "id" : "CDT_F5_P1",
            "name" : "F5",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F5_C1",
            "name" : "F5",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F5_R1",
            "name" : "F5",
            "visible" : 0,
            "children" : []
        }
        ]
    },
    {
        "id" : "CDT_F6",
        "name" : "F6",
        "visible" : 0,
        "children" :[
        {
            "id" : "CDT_F6_P1",
            "name" : "F6",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F6_C1",
            "name" : "F6",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F6_R1",
            "name" : "F6",
            "visible" : 0,
            "children" : []
        }
        ]
    },
    {
        "id" : "CDT_F7",
        "name" : "F7",
        "visible" : 0,
        "children" :[
        {
            "id" : "CDT_F7_P1",
            "name" : "F7",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F7_C1",
            "name" : "F7",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F7_R1",
            "name" : "F7",
            "visible" : 0,
            "children" : []
        }
        ]
    },
    {
        "id" : "CDT_F8",
        "name" : "F8",
        "visible" : 0,
        "children" :[
        {
            "id" : "CDT_F8_P1",
            "name" : "F8",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F8_C1",
            "name" : "F8",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F8_R1",
            "name" : "F8",
            "visible" : 0,
            "children" : []
        }
        ]
    },
    {
        "id" : "CDT_F9",
        "name" : "F9",
        "visible" : 0,
        "children" :[
        {
            "id" : "CDT_F9_P1",
            "name" : "F9",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F9_C1",
            "name" : "F9",
            "visible" : 0,
            "children" : []
        },
        {
            "id" : "CDT_F9_R1",
            "name" : "F9",
            "visible" : 0,
            "children" : []
        }
        ]
    }
    ]
    }

    return CDT_Wrapper


def create_child_template():
    template = {
    "id" : "",
    "name" : "name",
    "visible" : 1,
    "parent_id" : "",
    "children" : [{
        "id" : "",
        "name" : "name",
        "visible" : 1,
        "parent_id" : "",
        "children" : [
        {
            "id" : "",
            "name" : "name",
            "visible" : 1,
            "parent_id" : "",
            "children" : [
            {
                "id" : "",
                "name" : "name",
                "visible" : 1,
                "parent_id" : "",
                "children" : [
                {
                    "id" : "",
                    "name" : "name",
                    "visible" : 1,
                    "parent_id" : "",
                    "children" : [
                    {
                        "id" : "",
                        "name" : "name",
                        "visible" : 1,
                        "parent_id" : "",
                        "children" : [
                        {
                            "id" : "",
                            "name" : "name",
                            "visible" : 1,
                            "parent_id" : "",
                            "children" : [
                            {
                                "id" : "",
                                "name" : "name",
                                "visible" : 1,
                                "parent_id" : "",
                                "children" : [
                                {
                                    "id" : "",
                                    "name" : "name",
                                    "visible" : 1,
                                    "parent_id" : "",
                                    "children" : []
                                }]
                            }]
                        }]  
                    }]
                }]
            }]
        }]
    }]
    }

    return template

'''
def create_child_template():
    template = {
    "id" : "",
    "name" : "name",
    "visible" : 1,
    "parent_id" : "",
    "children" : [1,2,3]
    }
    return template
'''

def get_Wrapper():
    wrapper = {
    "name": "Seeding Food Studies",
    "id" : "F0",
    "children" :[
    {
        "id" : "F1",
        "name" : "LAND USE PLANNING",
        "header_text" : "LAND USE PLANNING DEFINES AND DESIGNATES ZONES FOR FOOD GROWING AT ALL SCALES",
        "content_text" : "There are currently 150 people and 37 projects and 5 courses that deal with this topic.",
        "color" : "8CC63F",
        "children" : [{
                "id" : "F1_P1",
                "name" : "PEOPLE",
                "header_text" : "",
                "content_text" : "",
                "color" : "8CC63F",
                "children" : [{
                    "id" : "F1_P1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "8CC63F",
                    "size" : 0,
                    "content" : []
                }]
            },
            {
                "id" : "F1_C1",
                "name" : "COURSES",
                "header_text" : "",
                "content_text" : "",
                "color" : "A2D165",
                "children" : [{
                    "id" : "F1_C1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "A2D165",
                    "size" : 0,
                    "content" : []
                }]
            },
            {
                "id" : "F1_R1",
                "name" : "PROJECTS",
                "header_text" : "",
                "content_text" : "",
                "color" : "B9DC8B",
                "children" : [{
                    "id" : "F1_R1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "B9DC8B",
                    "size" : 0,
                    "content" : []
                }]
            }]
    },
    {
        "id" : "F2",
        "name" : "SUITABILITY & SOIL SCIENCE",
        "header_text" : "SOIL SCIENCE FOCUSES ON SOIL AS A NATURAL RESOURCE ESSENTIAL TO FOOD PRODUCTION",
        "content_text" : "",
        "color" : "98C21F",
        "children" : [{
                "id" : "F2_P1",
                "name" : "PEOPLE",
                "header_text" : "",
                "content_text" : "",
                "color" : "98C21F",
                "children" : [{
                    "id" : "F2_P1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "98C21F",
                    "size" : 0,
                    "content" : []
                }]
            },
            {
            "id" : "F2_C1",
            "name" : "COURSES",
            "header_text" : "",
            "content_text" : "",
            "color" : "ACCE49",
            "children" : [{
                "id" : "F2_C1_I1",
                "name" : "name",
                "header_text" : "",
                "content_text" : "",
                "color" : "ACCE49",
                "size" : 0,
                "content" : []
            }]
        },
            {
                "id" : "F2_R1",
                "name" : "PROJECTS",
                "header_text" : "",
                "content_text" : "",
                "color" : "C1DA77",
                "children" : [{
                    "id" : "F2_R1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "C1DA77",
                    "size" : 0,
                    "content" : []
                }]
            }]
    },
    {
        "id" : "F3",
        "name" : "PRODUCTION & HARVESTING",
        "header_text" : "FARMING OCCURS AT MANY SCALES AND RELIES ON COMPLEX ECOLOGICAL, POLITICAL, AND ECONOMIC RELATIONSHIPS",
        "content_text" : "",
        "color" : "BAD636",
        "children" : [{
                "id" : "F3_P1",
                "name" : "PEOPLE",
                "header_text" : "",
                "content_text" : "",
                "color" : "BAD636",
                "children" : [{
                    "id" : "F3_P1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "BAD636",
                    "size" : 0,
                    "content" : []
                }]
            },
            {
                "id" : "F3_C1",
                "name" : "COURSES",
                "header_text" : "",
                "content_text" : "",
                "color" : "C6DF5D",
                "children" : [{
                    "id" : "F3_C1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "size" : 0,
                    "color" : "C6DF5D",
                    "content" : []
                }]
            },
            {
                "id" : "F3_R1",
                "name" : "PROJECTS",
                "header_text" : "",
                "content_text" : "",
                "color" : "D4E785",
                "children" : [{
                    "id" : "F3_R1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "D4E785",
                    "size" : 0,
                    "content" : []
                }]
            }]
    },
    {
        "id" : "F4",
        "name" : "TRANSPORTATION & DISTRIBUTION",
        "header_text" : "FOOD DISTRIBUTION INFRASTRUCTURE ALLOWS FOOD TO TRAVEL BETWEEN PRODUCER, PROCESSOR, AND CONSUMER",
        "content_text" : "",
        "color" : "909A34",
        "children" : [{
                "id" : "F4_P1",
                "name" : "PEOPLE",
                "header_text" : "",
                "content_text" : "",
                "color" : "909A34",
                "children" : [{
                    "id" : "F4_P1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "909A34",
                    "size" : 0,
                    "content" : []
                }]
            },
            {
                "id" : "F4_C1",
                "name" : "COURSES",
                "header_text" : "",
                "content_text" : "",
                "color" : "A6AE5D",
                "children" : [{
                    "id" : "F4_C1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "A6AE5D",
                    "size" : 0,
                    "content" : []
                }]
            },
            {
                "id" : "F4_R1",
                "name" : "PROJECTS",
                "header_text" : "",
                "content_text" : "",
                "color" : "BCC285",
                "children" : [{
                    "id" : "F4_R1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "BCC285",
                    "size" : 0,
                    "content" : []
                }]
            }]
    },
    {
        "id" : "F5",
        "name" : "AGGREGATION",
        "header_text" : "AGGREGATION COMBINES THE PRODUCE OF MULTIPLE FOOD GROWERS INTO LARGER VOLUME SUPPLY STREAMS",
        "content_text" : "",
        "color" : "718455",
        "children" : [{
                "id" : "F5_P1",
                "name" : "PEOPLE",
                "header_text" : "",
                "content_text" : "",
                "color" : "718455",
                "children" : [{
                    "id" : "F5_P1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "size" : 0,
                    "color" : "718455",
                    "content" : []
                }]
            },
            {
                "id" : "F5_C1",
                "name" : "COURSES",
                "header_text" : "",
                "content_text" : "",
                "color" : "8D9C77",
                "children" : [{
                    "id" : "F5_C1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "size" : 0,
                    "color" : "8D9C77",
                    "content" : []
                }]
            },
            {
                "id" : "F5_R1",
                "name" : "PROJECTS",
                "header_text" : "",
                "content_text" : "",
                "color" : "A9B599",
                "children" : [{
                    "id" : "F5_R1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "size" : 0,
                    "color" : "A9B599",
                    "content" : []
                }]
            }]
    },
    {
        "id" : "F6",
        "name" : "PROCESSING & MANUFACTURING",
        "header_text" : "PROCESSING AND MANUFACTURING INVOLVE ANY KIND OF COOKING, ALTERATION, OR RECOMBINING OF FOOD PRODUCTS",
        "content_text" : "",
        "color" : "6C6F5D",
        "children" : [{
                "id" : "F6_P1",
                "name" : "PEOPLE",
                "header_text" : "",
                "content_text" : "",
                "color" : "6C6F5D",
                "children" : [{
                    "id" : "F6_P1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "size" : 0,
                    "color" : "6C6F5D",
                    "content" : []
                }]
            },
            {
                "id" : "F6_C1",
                "name" : "COURSES",
                "header_text" : "",
                "content_text" : "",
                "color" : "898B7D",
                "children" : [{
                    "id" : "F6_C1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "size" : 0,
                    "color" : "898B7D",
                    "content" : []
                }]
            },
            {
                "id" : "F6_R1",
                "name" : "PROJECTS",
                "header_text" : "",
                "content_text" : "",
                "color" : "A7A89E",
                "children" : [{
                    "id" : "F6_R1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "A7A89E",
                    "size" : 0,
                    "content" : []
                }]
            }]
    },
    {
        "id" : "F7",
        "name" : "MARKETING & RETAIL",
        "header_text" : "MARKETING AND RETAIL COMMUNICATE AND DELIVER THE VALUE OF FOOD PRODUCTS TO CONSUMERS",
        "content_text" : "",
        "color" : "54531F",
        "children" : [{
                "id" : "F7_P1",
                "name" : "PEOPLE",
                "header_text" : "",
                "content_text" : "",
                "color" : "54531F",
                "children" : [{
                    "id" : "F7_P1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "54531F",
                    "size" : 0,
                    "content" : []
                }]
            },
            {
                "id" : "F7_C1",
                "name" : "COURSES",
                "header_text" : "",
                "content_text" : "",
                "color" : "75754C",
                "children" : [{
                    "id" : "F7_C1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "75754C",
                    "size" : 0,
                    "content" : []
                }]
            },
            {
                "id" : "F7_R1",
                "name" : "PROJECTS",
                "header_text" : "",
                "content_text" : "",
                "color" : "989779",
                "children" : [{
                    "id" : "F7_R1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "989779",
                    "size" : 0,
                    "content" : []
                }]
            }]
    },
    {
        "id" : "F8",
        "name" : "CONSUMPTION",
        "header_text" : "EATING FOOD IS AT ONCE SOCIAL, POLITICAL, NUTRITIONAL, AND FINANCIAL",
        "content_text" : "",
        "color" : "737245",
        "children" : [{
                "id" : "F8_P1",
                "name" : "PEOPLE",
                "header_text" : "",
                "content_text" : "",
                "color" : "737245",
                "children" : [{
                    "id" : "F8_P1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "737245",
                    "size" : 0,
                    "content" : []
                }]
            },
            {
                "id" : "F8_C1",
                "name" : "COURSES",
                "header_text" : "",
                "content_text" : "",
                "color" : "8F8D6A",
                "children" : [{
                    "id" : "F8_C1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "8F8D6A",
                    "size" : 0,
                    "content" : []
                }]
            },
            {
                "id" : "F8_R1",
                "name" : "PROJECTS",
                "header_text" : "",
                "content_text" : "",
                "color" : "ABAA8F",
                "children" : [{
                    "id" : "F8_R1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "ABAA8F",
                    "size" : 0,
                    "content" : []
                }]
            }]
    },
    {
        "id" : "F9",
        "name" : "RESOURCE & WASTE RECOVERY",
        "header_text" : "WASTE RECOVERY EXAMINES ALL FOOD WASTE, LOOKING FOR NEW VALUE IN WHAT WE THROW AWAY",
        "content_text" : "",
        "color" : "A8B396",
        "children" : [{
                "id" : "F9_P1",
                "name" : "PEOPLE",
                "header_text" : "",
                "content_text" : "",
                "color" : "A8B396",
                "children" : [{
                    "id" : "F9_P1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "A8B396",
                    "size" : 0,
                    "content" : []
                }]
            },
            {
                "id" : "F9_C1",
                "name" : "COURSES",
                "header_text" : "",
                "content_text" : "",
                "color" : "B9C2AA",
                "children" : [{
                    "id" : "F9_C1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "B9C2AA",
                    "size" : 0,
                    "content" : []
                }]
            },
            {
                "id" : "F9_R1",
                "name" : "PROJECTS",
                "header_text" : "",
                "content_text" : "",
                "color" : "CAD1BF",
                "children" : [{
                    "id" : "F9_R1_I1",
                    "name" : "name",
                    "header_text" : "",
                    "content_text" : "",
                    "color" : "CAD1BF",
                    "size" : 0,
                    "content" : []
                }]
            }]
    }
    ]}
    return wrapper