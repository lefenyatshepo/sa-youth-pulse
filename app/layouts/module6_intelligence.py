# ============================================================
# SA YOUTH PULSE DASHBOARD
# Module 6 — Province Intelligence Cards
# Narrative layer: situation, solutions, funding
# ============================================================

PROVINCE_INTELLIGENCE = {
    "North West": {
        "tier": "CRISIS",
        "tier_color": "#C0392B",
        "unemployment": "58.8%",
        "neet": "52.1%",
        "female_neet": "57.3%",
        "situation": (
            "North West carries the highest youth unemployment in South Africa "
            "at 58.8% — nearly 6 in 10 young people have no work. The province "
            "is heavily dependent on mining but young people are largely excluded "
            "from the supply chain. Female exclusion is the worst in the country "
            "at 57.3% NEET, driven by limited economic infrastructure outside of "
            "Rustenburg and Mahikeng. Long-term unemployment is entrenched — "
            "more than half of jobseekers have been searching for over a year."
        ),
        "working": (
            "YES Programme is active across retail and mining services sectors. "
            "Harambee has a strong Rustenburg presence placing youth in first jobs. "
            "NYDA Mahikeng offers entrepreneurship grants up to R250,000. "
            "The Mining SETA runs learnerships in engineering and safety. "
            "Sun City resort creates hospitality demand currently underserved "
            "by local youth-owned businesses."
        ),
        "opportunities": (
            "Mining services SMEs — equipment maintenance, catering, and safety "
            "consulting can plug directly into existing mine supply chains with "
            "relatively low startup costs. Solar installation and maintenance "
            "businesses are in high demand as mines seek energy independence. "
            "The Moli and Mela recycling model — a 100% black women-owned enterprise "
            "already holding Sun City contracts — is proof that recycling co-ops work "
            "here. Maize and sunflower agri-processing in the agricultural belt "
            "north of Rustenburg offers export-grade opportunities."
        ),
        "funding": "IDC, NEF, NYDA Mahikeng, Mining SETA, Jobs Fund",
        "key_contact": "NYDA Mahikeng: 018 384 1000 | YES: yes4youth.co.za",
    },

    "Eastern Cape": {
        "tier": "CRISIS",
        "tier_color": "#C0392B",
        "unemployment": "54.3%",
        "neet": "49.8%",
        "female_neet": "54.1%",
        "situation": (
            "The Eastern Cape has the lowest labour participation rate in South Africa "
            "— fewer than 4 in 10 young people are even actively looking for work, "
            "suggesting widespread discouragement. Youth unemployment sits at 54.3% "
            "with deep rural pockets in the OR Tambo and Alfred Nzo districts where "
            "access to economic infrastructure is almost nonexistent. Despite hosting "
            "a world-class automotive corridor through VW and BMW component suppliers, "
            "young people are largely absent from that value chain."
        ),
        "working": (
            "YES Programme is active in retail, healthcare, and logistics. "
            "Harambee operates in East London and Port Elizabeth. "
            "East Cape Midlands TVET College runs automotive and engineering programmes. "
            "The Eastern Cape Development Corporation provides SME funding. "
            "Walter Sisulu University has strong community engagement programmes "
            "connecting graduates to local employment."
        ),
        "opportunities": (
            "Automotive parts supply SMEs can feed directly into the VW and BMW "
            "component supply chains based in Uitenhage and East London — these "
            "companies actively seek local B-BBEE suppliers. Agri-processing "
            "co-operatives in mohair, dairy, and citrus offer high value-add potential "
            "with export-grade produce. Coastal eco-tourism along the Wild Coast and "
            "Addo Elephant corridor is massively underserved by locally-owned operators. "
            "Last-mile rural delivery logistics is a critical gap given the province's "
            "vast geography and underserved communities."
        ),
        "funding": "IDC, Jobs Fund, NYDA, Eastern Cape Development Corporation",
        "key_contact": "NYDA East London: 043 743 9100 | YES: yes4youth.co.za",
    },

    "Limpopo": {
        "tier": "HIGH CONCERN",
        "tier_color": "#E67E22",
        "unemployment": "47.2%",
        "neet": "46.3%",
        "female_neet": "51.2%",
        "situation": (
            "Limpopo has high youth unemployment at 47.2% but benefits from a "
            "relatively lower crime rate compared to other high-unemployment provinces — "
            "suggesting that strong community structures and rural cohesion provide "
            "a buffer. The province has enormous untapped economic potential through "
            "its proximity to Kruger National Park, world-class avocado and citrus "
            "export agriculture, and a significant platinum and coal mining sector. "
            "The challenge is connecting young people to these opportunities."
        ),
        "working": (
            "YES Programme is active in mining and agriculture sectors. "
            "NYDA Polokwane provides entrepreneurship support and grants. "
            "The Mining SETA runs active learnerships in Lephalale and Mokopane. "
            "AgriSETA supports agricultural skills development across the province. "
            "Kruger National Park's concessionaires are increasingly required "
            "to source local youth talent."
        ),
        "opportunities": (
            "Safari and eco-tourism enterprises along the Kruger corridor are "
            "significantly underserved by locally-owned youth businesses — this is "
            "the single biggest untapped opportunity in the province. Avocado, mango, "
            "and citrus export-grade agri-processing can access premium global markets "
            "with the right cold-chain infrastructure. Mining services SMEs in "
            "Lephalale and Mokopane can plug into existing mine supply chains. "
            "EdTech delivery centres feeding TVET pipelines into the mining sector "
            "address a critical skills gap."
        ),
        "funding": "IDC, Mining SETA, AgriSETA, NYDA, Jobs Fund",
        "key_contact": "NYDA Polokwane: 015 291 3000 | YES: yes4youth.co.za",
    },

    "KwaZulu-Natal": {
        "tier": "HIGH CONCERN",
        "tier_color": "#E67E22",
        "unemployment": "42.1%",
        "neet": "41.2%",
        "female_neet": "46.8%",
        "situation": (
            "KwaZulu-Natal combines South Africa's largest farming sector with its "
            "second-largest manufacturing base and the continent's busiest port — "
            "yet youth unemployment sits at 42.1%. The province has a severe urban "
            "and rural divide with Durban's metro economy operating separately from "
            "deeply underdeveloped rural areas in northern KZN. High crime rates "
            "particularly in Durban and surrounding areas compound the exclusion "
            "of young people from economic participation."
        ),
        "working": (
            "YES Programme has one of its largest placement bases in KZN across "
            "manufacturing, retail, and logistics. Harambee operates strongly in "
            "Durban with BPO and call centre placements. NYDA Durban provides "
            "entrepreneurship support. The Durban ICC and tourism sector actively "
            "supports youth hospitality programmes."
        ),
        "opportunities": (
            "Port logistics and freight SMEs feeding into Durban's container terminal "
            "— Africa's busiest port — represent enormous opportunity for youth-owned "
            "businesses in clearing, forwarding, and last-mile delivery. Sugar "
            "agri-processing and alternative crop value chains offer diversification "
            "from the struggling sugar industry. Cultural and heritage tourism "
            "encompassing Zulu heritage sites and battlefield routes is globally "
            "competitive but underserved by local operators. Textile and fashion "
            "manufacturing co-operatives can leverage existing skills in the province."
        ),
        "funding": "IDC, NEF, Jobs Fund, NYDA, BPO SETA",
        "key_contact": "NYDA Durban: 031 301 0850 | Harambee: harambee.co.za",
    },

    "Mpumalanga": {
        "tier": "HIGH CONCERN",
        "tier_color": "#E67E22",
        "unemployment": "44.3%",
        "neet": "43.5%",
        "female_neet": "48.3%",
        "situation": (
            "Mpumalanga is South Africa's energy province — home to the majority of "
            "Eskom's coal-fired power stations — yet youth unemployment stands at 44.3%. "
            "The province faces a structural transition as coal power is phased out, "
            "creating both a risk and an opportunity for young people. Significant "
            "forestry and timber resources in the Lowveld offer value-chain potential "
            "that is currently underdeveloped. Proximity to Kruger National Park "
            "creates tourism opportunity that is underutilised by local youth."
        ),
        "working": (
            "YES Programme is active in energy and agriculture sectors. "
            "NYDA Nelspruit provides entrepreneurship grants and mentorship. "
            "The Energy SETA runs skills programmes for the power sector transition. "
            "AgriSETA supports forestry and agricultural development. "
            "Kruger concessionaires are increasingly required to source locally."
        ),
        "opportunities": (
            "Renewable energy projects — solar and wind installations replacing "
            "coal infrastructure — represent the single biggest job creation "
            "opportunity in the province over the next decade. Timber and forestry "
            "value-chain SMEs processing raw timber into furniture and construction "
            "materials can access both local and export markets. Vegetable farming "
            "and food processing supplying Gauteng's growing food demand leverages "
            "the province's fertile lowveld soils. Tourism experiences along the "
            "Panorama Route and Kruger are significantly underserved."
        ),
        "funding": "IDC, Energy SETA, AgriSETA, NYDA, Jobs Fund",
        "key_contact": "NYDA Nelspruit: 013 752 7470 | YES: yes4youth.co.za",
    },

    "Free State": {
        "tier": "HIGH CONCERN",
        "tier_color": "#E67E22",
        "unemployment": "43.1%",
        "neet": "42.1%",
        "female_neet": "47.2%",
        "situation": (
            "The Free State is South Africa's maize belt — producing the majority "
            "of the country's grain — yet youth unemployment sits at 43.1%. The "
            "province occupies a strategic position on the N1 and N3 corridors "
            "connecting Gauteng to Cape Town and Durban, creating logistics "
            "opportunity that is largely untapped by youth-owned businesses. "
            "Bloemfontein's government and services economy dominates but has "
            "limited private sector job creation for young people."
        ),
        "working": (
            "YES Programme is active in retail and government services sectors. "
            "NYDA Bloemfontein provides entrepreneurship support and grants. "
            "AgriSETA runs agricultural skills programmes across the province. "
            "The Free State Development Corporation provides SME funding. "
            "Central University of Technology has strong graduate placement programmes."
        ),
        "opportunities": (
            "Maize processing, grain storage, and agri-logistics SMEs can plug "
            "directly into the province's dominant agricultural economy with "
            "relatively low startup costs. Road freight logistics along the N1 "
            "and N3 corridors offers consistent demand for youth-owned transport "
            "and warehousing businesses. Affordable housing construction feeding "
            "into the government pipeline provides reliable contract revenue. "
            "Renewable energy — solar and wind farms leveraging the flat terrain "
            "and high solar irradiation — represents growing opportunity."
        ),
        "funding": "IDC, AgriSETA, NYDA, Free State Development Corporation",
        "key_contact": "NYDA Bloemfontein: 051 411 4200 | YES: yes4youth.co.za",
    },

    "Northern Cape": {
        "tier": "HIGH CONCERN",
        "tier_color": "#E67E22",
        "unemployment": "40.2%",
        "neet": "38.9%",
        "female_neet": "43.1%",
        "situation": (
            "The Northern Cape is South Africa's largest province by land area but "
            "has the smallest population — creating unique dynamics where sparse "
            "infrastructure limits youth opportunity despite relatively lower "
            "unemployment at 40.2%. The province has the highest solar irradiation "
            "in South Africa, hosts the Square Kilometre Array telescope — a global "
            "science landmark — and has world-class diamond and manganese mining. "
            "The challenge is that most economic activity bypasses local youth."
        ),
        "working": (
            "YES Programme is active in mining and retail sectors. "
            "NYDA Kimberley provides entrepreneurship support and grants. "
            "The Mining SETA runs learnerships in diamond and manganese operations. "
            "The SKA project creates science and technology skills demand. "
            "Northern Cape Economic Development Agency provides SME support."
        ),
        "opportunities": (
            "Solar energy farms and installation services are the highest-potential "
            "opportunity in the province — the Northern Cape receives more solar "
            "irradiation than almost anywhere on earth and is central to South Africa's "
            "renewable energy transition. Science and astronomy tourism anchored by "
            "the SKA telescope is a globally unique drawcard that no other province "
            "can replicate. Diamond beneficiation and gemstone craft enterprises "
            "offer high-value artisan opportunities. Desert adventure and eco-tourism "
            "along the Augrabies and Namaqualand corridors is significantly underdeveloped."
        ),
        "funding": "IDC, Mining SETA, NYDA, Northern Cape EDA, Jobs Fund",
        "key_contact": "NYDA Kimberley: 053 832 6200 | YES: yes4youth.co.za",
    },

    "Gauteng": {
        "tier": "STABILISE",
        "tier_color": "#27AE60",
        "unemployment": "38.4%",
        "neet": "35.2%",
        "female_neet": "39.4%",
        "situation": (
            "Gauteng contributes 33% of South Africa's GDP yet has the highest "
            "absolute number of unemployed youth in the country — simply because "
            "it has the largest youth population. Unemployment at 38.4% is lower "
            "than most provinces but the sheer scale means millions of young people "
            "remain excluded. The province has the most active programme ecosystem "
            "in the country with Harambee institutionalised as an official government "
            "partner and the Microsoft AI Skills Platform targeting 300,000 youth."
        ),
        "working": (
            "Harambee is institutionalised by the Gauteng Provincial Government "
            "as an official labour market partner. YES Programme has its largest "
            "national placement base in Gauteng. Microsoft AI Skills Platform "
            "is targeting 300,000 youth in digital skills. NYDA Johannesburg "
            "and Pretoria provide extensive entrepreneurship support. "
            "WeThinkCode and HyperionDev run coding bootcamps with strong "
            "employment placement rates."
        ),
        "opportunities": (
            "Tech startups and digital services businesses have the lowest startup "
            "cost and highest job creation rate per R100K invested of any sector "
            "in the province. Township retail and e-commerce fulfilment hubs "
            "serving the 14 million residents of Gauteng's townships represent "
            "a massive underserved market. Fintech and financial services startups "
            "can leverage Johannesburg's position as Africa's financial capital. "
            "Co-working and youth entrepreneurship campuses create ecosystem "
            "infrastructure that multiplies impact across all other sectors."
        ),
        "funding": "IDC, NEF, Microsoft, NYDA, Gauteng Enterprise Propeller",
        "key_contact": "NYDA Johannesburg: 011 651 7000 | Harambee: harambee.co.za",
    },

    "Western Cape": {
        "tier": "STABILISE",
        "tier_color": "#27AE60",
        "unemployment": "27.3%",
        "neet": "24.6%",
        "female_neet": "28.1%",
        "situation": (
            "The Western Cape has the lowest youth unemployment in South Africa at "
            "27.3% and is on an improving trend — but this masks a serious challenge. "
            "Despite low unemployment, the province has the highest crime index in "
            "the country driven by gang activity, inequality, and urbanisation in "
            "Cape Town's townships. The model that works here needs to be documented "
            "and exported to other provinces — the Western Cape is proof that "
            "coordinated intervention can move the needle."
        ),
        "working": (
            "YES Programme and Harambee both operate strongly in the province. "
            "NYDA Cape Town provides extensive entrepreneurship support. "
            "WeThinkCode Cape Town is producing world-class software developers. "
            "The Cape Town tech ecosystem — Africa's Silicon Cape — is a global "
            "benchmark. Wine and agri-tourism industries have strong youth "
            "employment pipelines through hospitality training programmes."
        ),
        "opportunities": (
            "Scaling Cape Town's tech hub into a pan-African Silicon Cape ecosystem "
            "creates multiplier effects across all sectors. The blue economy — "
            "aquaculture, ocean logistics, and marine services — is significantly "
            "underdeveloped relative to the province's coastline assets. "
            "Wine tourism and food experience businesses can leverage the province's "
            "global brand recognition. Exporting the Western Cape model to other "
            "provinces through mentorship programmes and knowledge transfer creates "
            "national impact while building local reputation."
        ),
        "funding": "IDC, Jobs Fund, NYDA, Western Cape Economic Development Partnership",
        "key_contact": "NYDA Cape Town: 021 418 5678 | YES: yes4youth.co.za",
    },
}


def get_intelligence_card(province):
    if province not in PROVINCE_INTELLIGENCE:
        return None
    return PROVINCE_INTELLIGENCE[province]


def get_all_provinces():
    return list(PROVINCE_INTELLIGENCE.keys())