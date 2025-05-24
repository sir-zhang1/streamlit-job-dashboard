import streamlit as st
import pandas as pd
import plotly.express as px

# --- 页面基础设置 ---
st.set_page_config(page_title="长三角就业看板", layout="wide")
st.title("📊 长三角核心城市数字经济就业与技能需求看板")
st.write("---")

# --- 1. 构建技能映射字典 (基于你的附录，这里是一个示例) ---
skill_map = {
    # 后端开发 (部分) [cite: 38, 39, 40, 41, 42, 43]
        'java':  '后端开发',
        'python': '后端开发',
        'c++': '后端开发',
        'c#': '后端开发',
        'go': '后端开发',
        'php': '后端开发',
        'spring': '后端开发',
        'springboot': '后端开发',
        'spring boot': '后端开发',
        'restful': '后端开发',
        'restful api': '后端开发',
        'node.js': '后端开发',
        'nodejs': '后端开发',
        'node': '后端开发',
        'django': '后端开发',
        'flask': '后端开发',
        'api': '后端开发',
        'ruby': '后端开发',
        'scala': '后端开发',
        'golang': '后端开发',
        'dotnet': '后端开发',
        '.net': '后端开发',
        'webservice': '后端开发',
        'web service': '后端开发',
        'rust': '后端开发',
        'servlet': '后端开发',
        'springcloud': '后端开发',
        'spring cloud': '后端开发',
        'tomcat': '后端开发',
        'netty': '后端开发',
        'dubbo': '后端开发',
        'fastapi': '后端开发',
        'c/c++': '后端开发', 
        'c': '后端开发',
        'asp.net': '后端开发',
        'fastapi': '后端开发',
        'koa': '后端开发',
        'express': '后端开发',
        'gin': '后端开发',
        'laravel': '后端开发',
        'struts': '后端开发',
        'hibernate': '后端开发',
        'microservices': '后端开发',
        '微服务': '后端开发',
        'linux': '后端开发',
        'docker': '后端开发',
        'nginx': '后端开发',
        'shell': '后端开发',
        'jvm': '后端开发',
        'git': '后端开发',
        '微服务架构': '后端开发',
        '分布式技术': '后端开发',
        '分布式系统': '后端开发',
        '分布式': '后端开发',
        '网络协议': '后端开发',
        'mvc': '后端开发',
        'mvc开发': '后端开发',
        'http': '后端开发',
        'tcp/ip': '后端开发',
        'tcp': '后端开发',
        'ip': '后端开发',
        'unix': '后端开发',
        'devops': '后端开发',
        'cicd': '后端开发',
        'ci/cd': '后端开发',
        'jenkins': '后端开发',


    # 前端开发 (部分) [cite: 44, 45, 46, 47, 48]
        'javascript': '前端开发',
        'js': '前端开发',
        'html': '前端开发',
        'css': '前端开发',
        'html5': '前端开发',
        'css3': '前端开发',
        'react': '前端开发',
        'vue': '前端开发',
        'vue.js': '前端开发',
        'vuejs': '前端开发',
        'react.js': '前端开发',
        'reactjs': '前端开发',
        'angular': '前端开发',
        'jquery': '前端开发',
        'bootstrap': '前端开发',
        'typescript': '前端开发',
        'ts': '前端开发',
        'webpack': '前端开发',
        'less': '前端开发',
        'sass': '前端开发',
        'scss': '前端开发',
        'elementui': '前端开发',
        'element ui': '前端开发',
        'antd': '前端开发',
        'ant design': '前端开发',
        'redux': '前端开发',
        'flutter': '前端开发',
        'uni-app': '前端开发',
        'uniapp': '前端开发',
        'weapp': '前端开发',
        'miniprogram': '前端开发',
        'electron': '前端开发',
        'next.js': '前端开发',
        'nextjs': '前端开发',
        'wpf': '前端开发',
        'qt': '前端开发', 
        'winform': '前端开发',
        'tailwind': '前端开发',
        'echarts': '前端开发',
        'd3.js': '前端开发',
        'd3': '前端开发',
        'vite': '前端开发',
        'npm': '前端开发',
        'yarn': '前端开发',
        'gulp': '前端开发',
        '小程序': '前端开发',
        '移动端': '前端开发',
        'h5': '前端开发',
        'h5开发': '前端开发',
        'web前端': '前端开发',
        'web开发': '前端开发',
        'ui设计': '前端开发',
        'ux设计': '前端开发',
        'ui/ux': '前端开发',

    # 测试 (部分) [cite: 49, 50, 51, 52]
         '测试': '测试',
        'test': '测试',
        'junit': '测试',
        'selenium': '测试',
        'jmeter': '测试',
        'testng': '测试',
        'mockito': '测试',
        'mock': '测试',
        '自动化测试': '测试',
        '功能测试': '测试',
        '性能测试': '测试',
        '接口测试': '测试',
        'api测试': '测试',
        'ui测试': '测试',
        'ui自动化': '测试',
        'qa': '测试',
        'postman': '测试',
        'charles': '测试',
        'appium': '测试',
        '单元测试': '测试',
        '集成测试': '测试',
        '压力测试': '测试',
        'pytest': '测试',
        'cucumber': '测试',
        'mocha': '测试',
        'jest': '测试',
        'jasmine': '测试',
        'cypress': '测试',
        'loadrunner': '测试',
        'bugfree': '测试',
        'mantis': '测试',
        'jira': '测试',
        'bug管理': '测试',
        '冒烟测试': '测试',
        '回归测试': '测试',
        '黑盒测试': '测试',
        '白盒测试': '测试',
        '嵌入式测试': '测试',
        '系统测试': '测试',
        '软件测试理论': '测试',
        '软件测试流程': '测试',
        '测试理论': '测试',
        '测试流程': '测试',
        '软件测试': '测试',
        '测试开发': '测试',
        'fiddler': '测试',
        'wireshark': '测试',
        '渗透测试': '测试',
        '安全测试': '测试',
        '兼容性测试': '测试',
        '移动端测试': '测试',
        'app测试': '测试',
        'web测试': '测试',
        '测试用例': '测试',
        '测试计划': '测试',
        '测试报告': '测试',
        '测试工具': '测试',
        '测试框架': '测试',
        '测试脚本': '测试',
        '测试管理': '测试',
        '测试设计': '测试',
        '测试分析': '测试',
        '测试执行': '测试',
        '测试环境': '测试',
        '测试数据': '测试',
        '测试策略': '测试',
        '测试方法': '测试',
        '测试标准': '测试',
        '测试规范': '测试',
        '测试工程师': '测试',
        'robotframework': '测试',
        'gatling': '测试',
        'soap ui': '测试',
        'soapui': '测试',
        'testlink': '测试',
        'xmind': '测试',
        'bug跟踪': '测试',
        '缺陷管理': '测试',
        '质量保证': '测试',
        '质量控制': '测试',
        'qc': '测试',
        'quality center': '测试',


    # 数据库 (部分) [cite: 53, 54, 55, 56]
     'sql': '数据库',
        'mysql': '数据库',
        'oracle': '数据库',
        'postgresql': '数据库',
        'mongodb': '数据库',
        'redis': '数据库',
        'elasticsearch': '数据库',
        'es': '数据库',
        'sqlserver': '数据库',
        'sql server': '数据库',
        'nosql': '数据库',
        'db2': '数据库',
        'mariadb': '数据库',
        'sqlite': '数据库',
        'hbase': '数据库',
        'cassandra': '数据库',
        'neo4j': '数据库',
        'dynamodb': '数据库',
        'memcached': '数据库',
        'influxdb': '数据库',
        'tidb': '数据库',
        'etl': '数据库',
        'mybatis': '数据库',
        'jdbc': '数据库',
        'jpa': '数据库',
        'hibernate': '数据库',
        'database': '数据库',
        '数据库': '数据库',
        'pl/sql': '数据库',
        'plsql': '数据库',
        't-sql': '数据库',
        'tsql': '数据库',
        'couchdb': '数据库',
        'mongodb': '数据库',
        'dbms': '数据库',
        'relational database': '数据库',
        '关系型数据库': '数据库',
        '数据库开发': '数据库',
        '数据库设计': '数据库',
        '数据库管理': '数据库',
        '数据库优化': '数据库',


    # 大数据 (部分) [cite: 57, 58, 59, 60]
    'hadoop': '大数据',
        'spark': '大数据',
        'hive': '大数据',
        'kafka': '大数据',
        'flink': '大数据',
        'storm': '大数据',
        'zookeeper': '大数据',
        'flume': '大数据',
        'sqoop': '大数据',
        'kylin': '大数据',
        'hdfs': '大数据',
        'mapreduce': '大数据',
        'yarn': '大数据',
        'presto': '大数据',
        'druid': '大数据',
        'impala': '大数据',
        'datawarehouse': '大数据',
        '数据仓库': '大数据',
        'etl': '大数据',
        '数据建模': '大数据',
        'olap': '大数据',
        'oltp': '大数据',
        'datax': '大数据',
        'airflow': '大数据',
        'azkaban': '大数据',
        'oozie': '大数据',
        'big data': '大数据',
        '大数据': '大数据',
        '数据分析': '大数据',
        '数据挖掘': '大数据',
        'data mining': '大数据',
        'data analysis': '大数据',
        'bi': '大数据',
        'tableau': '大数据',
        'powerbi': '大数据',
        'power bi': '大数据',
        'quickbi': '大数据',
        'superset': '大数据',
        'clickhouse': '大数据',
        'excel': '大数据',
        'spss': '大数据',
        'sas': '大数据',
        'stata': '大数据',
        '大数据开发': '大数据',
        '大数据分析': '大数据',
        '大数据处理': '大数据',

    # 人工智能/机器学习 (部分) [cite: 61, 62, 63, 64, 65]
   'ai': '人工智能/机器学习',
        '人工智能': '人工智能/机器学习',
        'ml': '人工智能/机器学习',
        '机器学习': '人工智能/机器学习',
        '深度学习': '人工智能/机器学习',
        'deep learning': '人工智能/机器学习',
        'nlp': '人工智能/机器学习',
        '自然语言处理': '人工智能/机器学习',
        'cv': '人工智能/机器学习',
        '计算机视觉': '人工智能/机器学习',
        'tensorflow': '人工智能/机器学习',
        'pytorch': '人工智能/机器学习',
        'keras': '人工智能/机器学习',
        'scikit-learn': '人工智能/机器学习',
        'sklearn': '人工智能/机器学习',
        'paddlepaddle': '人工智能/机器学习',
        'caffe': '人工智能/机器学习',
        'mxnet': '人工智能/机器学习',
        'xgboost': '人工智能/机器学习',
        'lightgbm': '人工智能/机器学习',
        'cnn': '人工智能/机器学习',
        'rnn': '人工智能/机器学习',
        'lstm': '人工智能/机器学习',
        'gan': '人工智能/机器学习',
        'llm': '人工智能/机器学习',
        'gpt': '人工智能/机器学习',
        'bert': '人工智能/机器学习',
        'transformer': '人工智能/机器学习',
        '图像识别': '人工智能/机器学习',
        '语音识别': '人工智能/机器学习',
        '推荐系统': '人工智能/机器学习',
        'recommendation': '人工智能/机器学习',
        'halcon': '人工智能/机器学习', # 添加计算机视觉相关
        'opengl': '人工智能/机器学习', # 添加图形处理相关
        'directx': '人工智能/机器学习', # 添加图形处理相关
        '图形渲染': '人工智能/机器学习', # 添加图形处理相关
        'cae': '人工智能/机器学习', # 计算机辅助工程
        'opencascade': '人工智能/机器学习', # 3D建模引擎
        'machine learning': '人工智能/机器学习',
        'artificial intelligence': '人工智能/机器学习',
        'computer vision': '人工智能/机器学习',
        'natural language processing': '人工智能/机器学习',
        '神经网络': '人工智能/机器学习',
        '神经网络': '人工智能/机器学习',
        '强化学习': '人工智能/机器学习',
        '强化学习': '人工智能/机器学习',
        'torch': '人工智能/机器学习',
        'yolo': '人工智能/机器学习',
        'svm': '人工智能/机器学习',
        'random forest': '人工智能/机器学习',
        '随机森林': '人工智能/机器学习',
        '决策树': '人工智能/机器学习',
}

# --- 2. 数据加载与处理函数 ---
CLEANED_DATA_PATH = 'd:\\编程\\招聘数据小demo\\招聘数据_清洗后.csv'
EXPLODED_DATA_PATH = 'd:\\编程\\招聘数据小demo\\招聘数据_技能展开.csv'

@st.cache_data # 缓存数据
def load_and_process_data(cleaned_path, exploded_path, skill_mapping):
    try:
        df = pd.read_csv(cleaned_path)
        df_exploded = pd.read_csv(exploded_path)

        df['salary_avg_annual_wy'] = pd.to_numeric(df['salary_avg_annual_wy'], errors='coerce')
        df_exploded['skill_single'] = df_exploded['skill_single'].dropna().astype(str).str.lower() # 确保小写

        # *** 新增：应用技能分类映射 ***
        df_exploded['skill_category'] = df_exploded['skill_single'].map(skill_mapping).fillna('其他')

        return df, df_exploded
    except FileNotFoundError:
        st.error(f"错误：找不到数据文件。请确保 '{cleaned_path}' 和 '{exploded_path}' 存在。")
        return None, None

df, df_exploded = load_and_process_data(CLEANED_DATA_PATH, EXPLODED_DATA_PATH, skill_map)

# --- 检查数据是否加载成功 ---
if df is not None and df_exploded is not None:

    # --- 侧边栏 ---
    st.sidebar.header("⚙️ 控制面板")
    cities = df['city'].unique()
    
    # --- 3. 创建标签页 ---
    tab1, tab2 = st.tabs(["📈 城市概览", "📊 技能对比"])

    # --- 标签页1：城市概览 ---
    with tab1:
        st.header("单个城市就业市场深度观察")
        selected_city_overview = st.sidebar.selectbox("选择一个城市进行查看：", cities, key="overview_city")

        city_data = df[df['city'] == selected_city_overview]
        city_skills_exploded = df_exploded[df_exploded['city'] == selected_city_overview]

        st.subheader(f"📍 {selected_city_overview} 市场概览")
            # <<< 在这里添加文字 (1) >>>
        st.markdown(f"""
        本部分深入展示 **{selected_city_overview}** 的数字经济就业市场关键特征。
        了解单个城市的薪酬水平、人才构成及核心技能需求，有助于把握区域发展动态。
        """)
# <<< 添加结束 >>>
        avg_salary = city_data['salary_avg_annual_wy'].mean()
        # <<< 在这里添加文字 (2) >>>
        st.markdown(f"**{selected_city_overview}** 的数字经济相关岗位提供了一个具有竞争力的薪酬水平。以下是根据我们样本估算的平均年薪：")
        # <<< 添加结束 >>>
        st.metric(label="估算平均年薪 (万元)", value=f"{avg_salary:.2f}" if pd.notna(avg_salary) else "N/A")
        st.write("---")

        col1a, col2a = st.columns(2)
        with col1a:
            st.subheader("🎓 学历要求分布")
            # <<< 在这里添加文字 (3) >>>
            st.markdown("学历是衡量劳动力素质的重要指标。下图揭示了该城市对不同学历层次人才的需求偏好。")
            # <<< 添加结束 >>>
            edu_counts = city_data['education'].value_counts()
            if not edu_counts.empty:
                fig_edu = px.pie(edu_counts, values=edu_counts.values, names=edu_counts.index, title='学历要求', hole=0.3)
                fig_edu.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig_edu, use_container_width=True)
                # <<< 在这里添加文字 (4) >>>
                st.markdown("""
                从学历分布来看，**本科学历** 是当前数字经济岗位的绝对主流需求。
                同时，对 **大专** 学历的需求也占有一定比例，而 **硕博** 及 **不限学历** 的岗位相对较少。
                """)
                # <<< 添加结束 >>>      
            else: st.warning("无学历数据。")

        with col2a:
            st.subheader("📈 经验要求分布")
            # <<< 在这里添加文字 (5) >>>
            st.markdown("工作经验反映了市场对即战力和成熟度的需求。下图展示了岗位对经验年限的具体要求。")
            # <<< 添加结束 >>>
            exp_counts = city_data['experience'].value_counts()
            if not exp_counts.empty:
                fig_exp = px.pie(exp_counts, values=exp_counts.values, names=exp_counts.index, title='工作经验要求', hole=0.3)
                fig_exp.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig_exp, use_container_width=True)
                # <<< 在这里添加文字 (6) >>>
                st.markdown("""
                市场需求高度集中在具备 **1-5年** 工作经验的人才，尤其是 **3-5年** 经验。
                这表明企业既需要有一定实践经验的骨干，也为初级人才提供了成长空间。
                """)
                # <<< 添加结束 >>>
            else: st.warning("无经验数据。")

        st.write("---")
        # <<< 在这里添加额外的空白行 >>>
        st.write("")  # 插入一个空白行，增加一点点间距
        st.markdown(" ") # 也可以用markdown插入一个空格，有时也能产生间距
        # st.write("")  # 如果觉得不够，可以再加一个
        # <<< 添加结束 >>>
        col1b, col2b = st.columns(2)
        with col1b:
            st.subheader("🛠️ Top 10 具体技能需求")
            # <<< 在这里添加文字 (7) >>>
            st.markdown("高频技能标签直接反映了当前企业最急需的技术能力，是技术栈的风向标。")
            # <<< 添加结束 >>>
            skill_counts = city_skills_exploded['skill_single'].value_counts().head(10).sort_values(ascending=True)
            if not skill_counts.empty:
                fig_skills = px.bar(skill_counts, x=skill_counts.values, y=skill_counts.index, orientation='h', title='Top 10 具体技能', labels={'x': '提及次数', 'y': '技能名称'}, text=skill_counts.values)
                st.plotly_chart(fig_skills, use_container_width=True)
            else: st.warning("该城市暂无技能数据记录。")
            
        with col2b:
            st.subheader("🗂️ 核心技能类别分布")
            # <<< 在这里添加文字 (8) >>>
            st.markdown("从更高维度看，技能类别的分布揭示了城市产业结构的特点，例如是偏重基础开发还是前沿应用。")
            # <<< 添加结束 >>>
            # *** 新增：技能类别分布图 ***
            category_counts = city_skills_exploded['skill_category'].value_counts()
            if not category_counts.empty:
                fig_cat = px.pie(category_counts, values=category_counts.values, names=category_counts.index, title='核心技能类别', hole=0.3)
                fig_cat.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig_cat, use_container_width=True)
            else: st.warning("该城市暂无技能类别数据记录。")


    # --- 标签页2：技能对比 ---
    with tab2:
        st.header("多城市技能需求横向对比")
        # <<< 在这里添加文字 (9) >>>
        st.markdown("""
        长三角地区各核心城市在数字经济发展上各有侧重。通过对比不同城市的技能需求，
        我们可以观察到它们在**产业布局、发展阶段和人才战略上的差异**。
        请在左侧选择您想对比的城市。
        """)
        # <<< 添加结束 >>>
        selected_cities_comparison = st.sidebar.multiselect(
            "选择要对比的城市 (可多选):",
            options=cities,
            default=list(cities)[:2], # 默认选前两个
            key="compare_cities"
        )

        if not selected_cities_comparison:
            st.warning("请至少选择一个城市进行对比。")
        else:
            comparison_data = df_exploded[df_exploded['city'].isin(selected_cities_comparison)]
            if comparison_data.empty:
                st.warning("所选城市无技能数据。")
            else:
                # --- 具体技能对比 ---
                st.subheader("Top 15 具体技能需求占比对比 (%)")
                skill_counts = comparison_data.groupby(['city', 'skill_single']).size().reset_index(name='count')
                city_totals = comparison_data.groupby('city').size().reset_index(name='total_skills')
                skill_proportions = pd.merge(skill_counts, city_totals, on='city')
                skill_proportions['proportion'] = (skill_proportions['count'] / skill_proportions['total_skills']) * 100
                overall_top_skills = df_exploded['skill_single'].value_counts().head(15).index.tolist()
                plot_data_skills = skill_proportions[skill_proportions['skill_single'].isin(overall_top_skills)]

                if not plot_data_skills.empty:
                    fig_compare_skills = px.bar(plot_data_skills, x='skill_single', y='proportion', color='city', barmode='group', title='Top 15 具体技能对比', labels={'skill_single': '技能名称', 'proportion': '技能提及占比 (%)', 'city': '城市'}, height=500)
                    fig_compare_skills.update_xaxes(tickangle=45)
                    st.plotly_chart(fig_compare_skills, use_container_width=True)
                else: st.info("所选城市在 Top 15 具体技能中没有重叠数据。")

                st.write("---")
                
                # --- 技能类别对比 ---
                st.subheader("核心技能类别需求占比对比 (%)")
                # *** 新增：技能类别对比图 ***
                category_counts_comp = comparison_data.groupby(['city', 'skill_category']).size().reset_index(name='count')
                # 注意：这里我们复用 city_totals
                category_proportions = pd.merge(category_counts_comp, city_totals, on='city')
                category_proportions['proportion'] = (category_proportions['count'] / category_proportions['total_skills']) * 100
                
                # 筛选掉 '其他' 类别，让对比更聚焦
                plot_data_cat = category_proportions[category_proportions['skill_category'] != '其他']

                if not plot_data_cat.empty:
                    fig_compare_cat = px.bar(plot_data_cat, x='skill_category', y='proportion', color='city', barmode='group', title='核心技能类别对比', labels={'skill_category': '技能类别', 'proportion': '技能提及占比 (%)', 'city': '城市'}, height=500)
                    st.plotly_chart(fig_compare_cat, use_container_width=True)
                else: st.info("所选城市无核心技能类别数据。")

        # <<< 在这里添加文字 (10) >>>
        st.markdown("""
        ---
        **分组柱状图解读小贴士**：
        * **具体技能对比**：关注那些在不同城市间**占比差异巨大**的技能，它们可能揭示了特定城市的特色产业或技术优势。例如，比较Java和Python在不同城市的占比。
        * **核心类别对比**：观察**后端开发、大数据、AI**等核心类别的整体占比，可以判断城市数字经济的成熟度和发展方向。
        """)
        # <<< 添加结束 >>>


else:
    st.error("数据未能成功加载，请检查文件路径和内容。")

# --- 页脚 ---
st.write("---")
st.caption("项目作者：张梦昂 | 数据来源：BOSS直聘 (2025.04) | 基于全国大学生统计建模大赛作品")