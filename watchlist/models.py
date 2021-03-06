# -*- coding: utf-8 -*-
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from watchlist import db


class User(db.Model, UserMixin):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class Videos(db.Model):  # 表名将会是videos
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(45))
    URL = db.Column(db.String(45))
    parallel_title = db.Column(db.String(45))
    alternate_title = db.Column(db.String(45))
    other_title_info = db.Column(db.String(45))
    series_title = db.Column(db.String(45))
    parallel_series_title = db.Column(db.String(45))
    individual_name = db.Column(db.String(45))
    group_name = db.Column(db.String(45))
    conference_name = db.Column(db.String(45))
    joint_author_name = db.Column(db.String(45))
    other_info = db.Column(db.String(45))
    bearing_method = db.Column(db.String(45))
    version = db.Column(db.String(45))
    public_date = db.Column(db.String(45))
    addi_block_type = db.Column(db.String(45))
    addi_block_desc = db.Column(db.String(45))
    sound_id = db.Column(db.String(45))
    sound_content = db.Column(db.String(45))
    notes = db.Column(db.String(45))
    search_method = db.Column(db.String(45))
    key_word = db.Column(db.String(45))
    sum = db.Column(db.String(45))
    system = db.Column(db.String(45))
    sound_chara = db.Column(db.String(45))
    colors = db.Column(db.String(45))
    resolution = db.Column(db.String(45))
    sound_qua = db.Column(db.String(45))
    frame_qua = db.Column(db.String(45))
    mode = db.Column(db.String(45))
    type = db.Column(db.String(45))
    depth = db.Column(db.String(45))
    video_sampling_frequency = db.Column(db.String(45))
    language_id = db.Column(db.String(45))
    language_type = db.Column(db.String(45))
    subtitle_id = db.Column(db.String(45))
    subtitle_type = db.Column(db.String(45))
    audience = db.Column(db.String(45))
    ori_form = db.Column(db.String(45))
    other_form = db.Column(db.String(45))
    inclusion = db.Column(db.String(45))
    included = db.Column(db.String(45))
    refering = db.Column(db.String(45))
    reference = db.Column(db.String(45))
    copyright_holder = db.Column(db.String(45))
    copyright_notice = db.Column(db.String(45))
    authorize_person = db.Column(db.String(45))
    authorize_form = db.Column(db.String(45))
    authorize_date = db.Column(db.String(45))
    authorize_due = db.Column(db.String(45))
    authorize_area = db.Column(db.String(45))
    authorize_file = db.Column(db.String(45))
    authorize_info = db.Column(db.String(45))
    time_length = db.Column(db.String(45))
    space_length = db.Column(db.String(45))
    source_carrier = db.Column(db.String(45))
    collect_area = db.Column(db.String(45))
    collect_unit = db.Column(db.String(45))
    call_number = db.Column(db.String(45))
    collect_person = db.Column(db.String(45))
    process_unit = db.Column(db.String(45))
    serve_form = db.Column(db.String(45))
    serve_column = db.Column(db.String(45))
    serve_time = db.Column(db.String(45))
    serve_addr = db.Column(db.String(45))
    serve_obj = db.Column(db.String(45))
    acce_time = db.Column(db.String(45))
    acce_form = db.Column(db.String(45))
    acce_person = db.Column(db.String(45))
    acce_opi = db.Column(db.String(45))
    acce_repo = db.Column(db.String(45))
    series = db.Column(db.String(45))
    episode = db.Column(db.String(45))
    total_episodes = db.Column(db.String(45))
    producer = db.Column(db.String(45))
    pro_loca = db.Column(db.String(45))
    resource = db.Column(db.String(45))
    provider = db.Column(db.String(45))
    video_date = db.Column(db.String(45))
    create_date = db.Column(db.String(45))
    release_date = db.Column(db.String(45))
    award = db.Column(db.String(45))
    performance_form = db.Column(db.String(45))
    program_type = db.Column(db.String(45))
    subtitle = db.Column(db.String(45))
    length = db.Column(db.String(45))
    aspect_ratio = db.Column(db.String(45))
    bit_rate = db.Column(db.String(45))
    sound_track = db.Column(db.String(45))
    data_rate = db.Column(db.String(45))
    total_bitrate = db.Column(db.String(45))
    audio_sampling_frequency = db.Column(db.String(45))
    size = db.Column(db.String(45))


class Pictures(db.Model):  # 表名将会是pictures
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(45))
    URL = db.Column(db.String(45))
    individual_name = db.Column(db.String(45))
    group_name = db.Column(db.String(45))
    pro_loca = db.Column(db.String(45))
    pic_date = db.Column(db.String(45))
    process_unit= db.Column(db.String(45))
    create_date = db.Column(db.String(45))
    release_date = db.Column(db.String(45))
    size = db.Column(db.String(45))
    resolution = db.Column(db.String(45))
    parallel_title = db.Column(db.String(45))
    alternate_title = db.Column(db.String(45))
    other_title_info = db.Column(db.String(45))
    conference_name = db.Column(db.String(45))
    joint_author_name = db.Column(db.String(45))
    other_info = db.Column(db.String(45))
    bearing_method = db.Column(db.String(45))
    version = db.Column(db.String(45))
    collect_person= db.Column(db.String(45))
    producer = db.Column(db.String(45))
    public_date = db.Column(db.String(45))
    award = db.Column(db.String(45))
    notes = db.Column(db.String(45))
    search_method = db.Column(db.String(45))
    key_word = db.Column(db.String(45))
    sum = db.Column(db.String(45))
    colors = db.Column(db.String(45))
    audience = db.Column(db.String(45))
    resource = db.Column(db.String(45))
    provider = db.Column(db.String(45))
    type = db.Column(db.String(45))
    inclusion = db.Column(db.String(45))
    included = db.Column(db.String(45))
    copyright_holder = db.Column(db.String(45))
    copyright_notice = db.Column(db.String(45))
    authorize_person = db.Column(db.String(45))
    authorize_form = db.Column(db.String(45))
    authorize_date = db.Column(db.String(45))
    authorize_due = db.Column(db.String(45))
    authorize_area = db.Column(db.String(45))
    authorize_file = db.Column(db.String(45))
    authorize_info = db.Column(db.String(45))
    time_length = db.Column(db.String(45))
    space_length = db.Column(db.String(45))
    source_carrier = db.Column(db.String(45))
    serve_form = db.Column(db.String(45))
    serve_column = db.Column(db.String(45))
    serve_time = db.Column(db.String(45))
    serve_addr = db.Column(db.String(45))
    serve_obj = db.Column(db.String(45))
    acce_time = db.Column(db.String(45))
    acce_form = db.Column(db.String(45))
    acce_person = db.Column(db.String(45))
    acce_opi = db.Column(db.String(45))
    acce_repo = db.Column(db.String(45))


class Records(db.Model):  # 表名将会是records
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(45))
    URL = db.Column(db.String(45))
    pro_loca = db.Column(db.String(45))
    provider = db.Column(db.String(45))
    record_date = db.Column(db.String(45))
    create_date = db.Column(db.String(45))
    total_episodes= db.Column(db.String(45))
    release_date = db.Column(db.String(45))
    singing_form = db.Column(db.String(45))
    sound_track = db.Column(db.String(45))
    size = db.Column(db.String(45))
    length = db.Column(db.String(45))
    bit_rate = db.Column(db.String(45))
    type = db.Column(db.String(45))
    mode = db.Column(db.String(45))
    parallel_title = db.Column(db.String(45))
    alternate_title = db.Column(db.String(45))
    other_title_info = db.Column(db.String(45))
    series_title = db.Column(db.String(45))
    parallel_series_title = db.Column(db.String(45))
    total_episodes = db.Column(db.String(45))
    episode = db.Column(db.String(45))
    individual_name = db.Column(db.String(45))
    group_name = db.Column(db.String(45))
    conference_name = db.Column(db.String(45))
    joint_author_name = db.Column(db.String(45))
    other_info = db.Column(db.String(45))
    bearing_method = db.Column(db.String(45))
    version = db.Column(db.String(45))
    producer = db.Column(db.String(45))
    public_date = db.Column(db.String(45))
    award = db.Column(db.String(45))
    singing_style = db.Column(db.String(45))
    parts = db.Column(db.String(45))
    perform_form = db.Column(db.String(45))
    notes = db.Column(db.String(45))
    search_method = db.Column(db.String(45))
    key_word = db.Column(db.String(45))
    perf_type = db.Column(db.String(45))
    perf_form = db.Column(db.String(45))
    sum = db.Column(db.String(45))
    mesh_point = db.Column(db.String(45))
    audio_sampling_frequency = db.Column(db.String(45))
    depth = db.Column(db.String(45))
    language_id = db.Column(db.String(45))
    language_type = db.Column(db.String(45))
    audience = db.Column(db.String(45))
    resource = db.Column(db.String(45))
    ori_form = db.Column(db.String(45))
    other_form = db.Column(db.String(45))
    inclusion = db.Column(db.String(45))
    included = db.Column(db.String(45))
    referring = db.Column(db.String(45))
    reference = db.Column(db.String(45))
    copyright_holder = db.Column(db.String(45))
    copyright_notice = db.Column(db.String(45))
    authorize_person = db.Column(db.String(45))
    authorize_form = db.Column(db.String(45))
    authorize_date = db.Column(db.String(45))
    authorize_due = db.Column(db.String(45))
    authorize_area = db.Column(db.String(45))
    authorize_file = db.Column(db.String(45))
    authorize_info = db.Column(db.String(45))
    time_length = db.Column(db.String(45))
    space_length = db.Column(db.String(45))
    source_carrier = db.Column(db.String(45))
    collect_person = db.Column(db.String(45))
    process_unit = db.Column(db.String(45))
    serve_form = db.Column(db.String(45))
    serve_column = db.Column(db.String(45))
    serve_time = db.Column(db.String(45))
    serve_addr = db.Column(db.String(45))
    serve_obj = db.Column(db.String(45))
    acce_time = db.Column(db.String(45))
    acce_form = db.Column(db.String(45))
    acce_person = db.Column(db.String(45))
    acce_opi = db.Column(db.String(45))
    acce_repo = db.Column(db.String(45))


class Documents(db.Model):  # 表名将会是records
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)  # 主键
    parallel_title = db.Column(db.String(45))
    alternate_title = db.Column(db.String(45))
    other_title_info = db.Column(db.String(45))
    individual_name = db.Column(db.String(45))
    group_name = db.Column(db.String(45))
    conference_name = db.Column(db.String(45))
    joint_author_name = db.Column(db.String(45))
    other_info = db.Column(db.String(45))
    bearing_method = db.Column(db.String(45))
    version = db.Column(db.String(45))
    pro_loca = db.Column(db.String(45))
    producer = db.Column(db.String(45))
    public_date = db.Column(db.String(45))
    catalog = db.Column(db.String(45))
    award = db.Column(db.String(45))
    notes = db.Column(db.String(45))
    search_method = db.Column(db.String(45))
    sum = db.Column(db.String(45))
    type = db.Column(db.String(45))
    audience = db.Column(db.String(45))
    inclusion = db.Column(db.String(45))
    included = db.Column(db.String(45))
    copyright_holder = db.Column(db.String(45))
    copyright_notice = db.Column(db.String(45))
    authorize_person = db.Column(db.String(45))
    authorize_form = db.Column(db.String(45))
    authorize_date = db.Column(db.String(45))
    authorize_due = db.Column(db.String(45))
    authorize_area = db.Column(db.String(45))
    authorize_file = db.Column(db.String(45))
    authorize_info = db.Column(db.String(45))
    time_length = db.Column(db.String(45))
    space_length = db.Column(db.String(45))
    source_carrier = db.Column(db.String(45))
    collect_area = db.Column(db.String(45))
    collect_unit = db.Column(db.String(45))
    call_number = db.Column(db.String(45))
    collect_person = db.Column(db.String(45))
    process_unit = db.Column(db.String(45))
    serve_form = db.Column(db.String(45))
    serve_column = db.Column(db.String(45))
    serve_time = db.Column(db.String(45))
    serve_addr = db.Column(db.String(45))
    serve_obj = db.Column(db.String(45))
    acce_time = db.Column(db.String(45))
    acce_form = db.Column(db.String(45))
    acce_person = db.Column(db.String(45))
    acce_opi = db.Column(db.String(45))
    acce_repo = db.Column(db.String(45))
    title = db.Column(db.String(45))
    URL = db.Column(db.String(100))
    create_date = db.Column(db.String(45))
    release_date = db.Column(db.String(45))
    resource = db.Column(db.String(45))
    provider = db.Column(db.String(45))
    key_word = db.Column(db.String(45))
    abstract = db.Column(db.String(45))
    size = db.Column(db.String(45))