# Now the new Generate Tab

import streamlit as st
from graph_data_generator import generators
import graph_data_generator as gdg

def generate_tab():

    with st.expander("Instructions"):
        st.write(
            """
        1. Import a file created from the ① Ideate or ② Design tabs 
        2. The mock graph data generator will automatically generate a .zip file containing .csv and .json files. The .csvs can be independently imported into any database that supports .csv imports. The .json file is specifically formatted for the Neo4j Data Importer.
        3. Download the .zip file
        4. Proceed to the '④ Data Importer' tab
        """
        )
    

    st.markdown("--------")

    # c1, c2 = st.tabs(["Copy & Paste", "Import File"])
    # with c1:

    st.write("Copy & Paste Arrows.app .JSON file")
    filename = st.text_input("Name of file", value="mock_data")
    txt = st.text_area("Paste arrows.app JSON here", height=500, help="Click out of the text area to generate the .zip file.")
    if txt is not None and txt != "":

        try:
            zip = gdg.generate(txt)
            if zip is None:
                st.warning('Unexpected problem generating file. Try an alternate JSON input')
            else:
                st.download_button(
                    label = "Download .zip file",
                    data = zip,
                    file_name = f"{filename}.zip",
                    mime = "text/plain"
                )
        except Exception as e:
            st.error(e)
            
    # with c2:
    #     uploaded_file = st.file_uploader("Upload an arrows JSON file", type="json")
    #     if uploaded_file is not None:
    #         # To convert to a string based IO:
    #         stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #         # To read file as string:
    #         current_file = stringio.read()

    #         # Save to session state
    #         st.session_state[MAPPINGS] = Mapping.empty()

    #         name = uploaded_file.name.split(".")[0]
    #         if current_file is not None:
    #             # TODO: Verfiy file is valid arrows JSON
    #             generators = st.session_state[GENERATORS]
    #             mapping = mapping_from_json(
    #                 current_file, 
    #                 generators)
    #             zip = generate_zip(mapping)
    #             st.download_button(
    #                 label = "Download .zip file",
    #                 data = zip,
    #                 file_name = f"{name}.zip",
    #                 mime = "text/plain"
    #             )
