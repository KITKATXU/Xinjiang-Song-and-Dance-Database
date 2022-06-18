# -*- coding: utf-8 -*-
from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
import re,os, sys,datetime,time
from watchlist import app, db
from watchlist.models import User, Videos, Pictures, Records, Documents
interface_path = os.path.dirname(__file__)
sys.path.insert(0, interface_path)

@app.route('/',methods=['GET', 'POST'])
def index():
    pnum = Pictures.query.count()
    dnum = Documents.query.count()
    inum = Videos.query.count()
    mnum = Records.query.count()
    if request.method == 'POST':
        search = request.form.get('search')  # 传入表单对应输入字段的 name 值
        search = "%"+search+"%"
        # 根据传进来的内容进行搜索
        user = User.query.first()  # 读取用户记录
        searchpics = Pictures.query.filter(Pictures.title.like(search)).order_by(Pictures.create_date.desc()).all()  # 图片
        searchdras = Videos.query.filter(Videos.series == "剧目").filter(Videos.title.like(search)).order_by(Videos.create_date.desc()).all()
        searchints = Videos.query.filter(Videos.series == "教程").filter(Videos.title.like(search)).order_by(Videos.create_date.desc()).all()
        searchmucs = Records.query.filter(Records.title.like(search)).order_by(Records.create_date.desc()).all()
        searchdocs = Documents.query.filter(Documents.title.like(search)).order_by(Documents.create_date.desc()).all()
        return render_template('index.html', user=user, instructions=searchints, dramas=searchdras, musics=searchmucs,
                            pictures=searchpics, documents=searchdocs, pnum=pnum, dnum=dnum, inum=inum, mnum=mnum)
    user = User.query.first()  # 读取用户记录
    pics = Pictures.query.order_by(Pictures.create_date.desc()).all()
    dramas = Videos.query.filter(Videos.series == "剧目").order_by(Videos.create_date.desc())
    instructions = Videos.query.filter(Videos.series == "教程").order_by(Videos.create_date.desc())
    musics = Records.query.order_by(Records.create_date.desc()).all()
    documents = Documents.query.order_by(Documents.create_date.desc()).all()
    return render_template('index.html', user=user, instructions=instructions, dramas=dramas, musics=musics,
                           pictures=pics, documents=documents, pnum=pnum, dnum=dnum, inum=inum, mnum=mnum)

@app.route('/indexpicture', methods=['GET', 'POST'])
def indexpicture():
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        search = request.form.get('search')  # 传入表单对应输入字段的 name 值
        search = "%"+search+"%"
        # 根据传进来的内容进行搜索
        user = User.query.first()  # 读取用户记录
        searchpics = Pictures.query.filter(Pictures.title.like(search)).order_by(Pictures.create_date.desc()).all()  # 图片
        return render_template('indexpicture.html', user=user, pictures=searchpics)

    user = User.query.first()  # 读取用户记录
    pics = Pictures.query.order_by(Pictures.create_date.desc()).all()  # 图片
    return render_template('indexpicture.html', user=user, pictures=pics)

@app.route('/indexmusic', methods=['GET', 'POST'])
def indexmusic():
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        search = request.form.get('search')  # 传入表单对应输入字段的 name 值
        search = "%"+search+"%"
        # 根据传进来的内容进行搜索
        user = User.query.first()  # 读取用户记录
        searchmucs = Records.query.filter(Records.title.like(search)).order_by(Records.create_date.desc()).all()
        return render_template('indexmusic.html', user=user, musics=searchmucs)

    user = User.query.first()  # 读取用户记录
    musics = Records.query.order_by(Records.create_date.desc()).all()  # 音频
    return render_template('indexmusic.html', user=user, musics=musics)

@app.route('/indexdrama', methods=['GET', 'POST'])
def indexdrama():
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        search = request.form.get('search')  # 传入表单对应输入字段的 name 值
        search = "%"+search+"%"
        # 根据传进来的内容进行搜索
        user = User.query.first()  # 读取用户记录
        searchdras = Videos.query.filter(Videos.series == "剧目").filter(Videos.title.like(search)).order_by(Videos.create_date.desc()).all()
        return render_template('indexdrama.html', user=user, dramas=searchdras)

    user = User.query.first()  # 读取用户记录
    dramas = Videos.query.filter(Videos.series == "剧目").order_by(Videos.create_date.desc())  # 剧目
    return render_template('indexdrama.html', user=user, dramas=dramas)

@app.route('/indexinstruction', methods=['GET', 'POST'])
def indexinstruction():
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        search = request.form.get('search')  # 传入表单对应输入字段的 name 值
        search = "%"+search+"%"
        # 根据传进来的内容进行搜索
        user = User.query.first()  # 读取用户记录
        searchints = Videos.query.filter(Videos.series == "教程").filter(Videos.title.like(search)).order_by(Videos.create_date.desc()).all()
        return render_template('indexinstruction.html', user=user, instructions=searchints)

    user = User.query.first()  # 读取用户记录
    instructions = Videos.query.filter(Videos.series == "教程").order_by(Videos.create_date.desc())
    return render_template('indexinstruction.html', user=user, instructions=instructions)

@app.route('/indexdocument', methods=['GET', 'POST'])
def indexdocument():
    if request.method == 'POST':  # 判断是否是 POST 请求
        # 获取表单数据
        search = request.form.get('search')  # 传入表单对应输入字段的 name 值
        search = "%"+search+"%"
        # 根据传进来的内容进行搜索
        user = User.query.first()  # 读取用户记录
        searchdocu = Documents.query.filter(Documents.title.like(search)).order_by(Documents.create_date.desc()).all()
        return render_template('indexdocument.html', user=user, documents=searchdocu)

    user = User.query.first()  # 读取用户记录
    documents = Documents.query.order_by(Documents.create_date.desc()).all()  # 音频
    return render_template('indexdocument.html', user=user, documents=documents)

@app.route('/instruction.html')
def instruction():
    name = request.args.get('name', default='*', type=str)
    user = User.query.first()  # 读取用户记录
    pics = Pictures.query.all()
    dramas = Videos.query.filter(Videos.series == "剧目")
    instructions = Videos.query.filter(Videos.series == "教程")
    musics = Records.query.all()
    documents = Documents.query.all()
    return render_template('instruction.html', user=user, instructions=instructions, dramas=dramas, musics=musics,
                           pictures=pics, documents=documents, name=name)

@app.route('/video.html')
def video():
    name = request.args.get('name', default='*', type=str)
    user = User.query.first()  # 读取用户记录
    pics = Pictures.query.all()
    dramas = Videos.query.filter(Videos.series == "剧目")
    instructions = Videos.query.filter(Videos.series == "教程")
    musics = Records.query.all()
    documents = Documents.query.all()
    return render_template('video.html', user=user, instructions=instructions, dramas=dramas, musics=musics,
                           pictures=pics, documents=documents, name=name)


@app.route('/music.html')
def music():
    name = request.args.get('name', default='*', type=str)
    user = User.query.first()  # 读取用户记录
    pics = Pictures.query.all()
    dramas = Videos.query.filter(Videos.series == "剧目")
    instructions = Videos.query.filter(Videos.series == "教程")
    musics = Records.query.all()
    documents = Documents.query.all()
    return render_template('music.html', user=user, instructions=instructions, dramas=dramas, musics=musics,
                           pictures=pics, documents=documents, name=name)


@app.route('/picture.html')
def picture():
    name = request.args.get('name', default='*', type=str)
    pdate = request.args.get('pic_date', default='*', type=str)
    user = User.query.first()  # 读取用户记录
    pics = Pictures.query.filter().all()
    dramas = Videos.query.filter(Videos.series == "剧目").all()
    instructions = Videos.query.filter(Videos.series == "教程").all()
    musics = Records.query.all()
    documents = Documents.query.all()
    return render_template('picture.html', user=user, instructions=instructions, dramas=dramas, musics=musics,
                           pictures=pics, documents=documents, name=name,pdate = pdate)

@app.route('/document.html')
def document():
    name = request.args.get('name', default='*', type=str)
    user = User.query.first()  # 读取用户记录
    pics = Pictures.query.all()
    dramas = Videos.query.filter(Videos.series == "剧目")
    instructions = Videos.query.filter(Videos.series == "教程")
    musics = Records.query.all()
    documents = Documents.query.all()
    return render_template('document.html', user=user, instructions=instructions, dramas=dramas, musics=musics,
                           pictures=pics, documents=documents, name=name)

@app.route('/editvideo<int:video_id>', methods=['GET', 'POST'])
@login_required
def editvideo(video_id):
    v = Videos.query.get_or_404(video_id)
    if request.method == 'POST':  # 处理编辑表单的提交请求
        title = request.form['title']
        #URL = request.form['URL']
        alternate_title = request.form['alternate_title']
        parallel_title = request.form['parallel_title']
        other_title_info = request.form['other_title_info']
        series_title = request.form['series_title']
        parallel_series_title = request.form['parallel_series_title']
        individual_name = request.form['individual_name']
        group_name = request.form['group_name']
        conference_name = request.form['conference_name']
        joint_author_name = request.form['joint_author_name']
        other_info = request.form['other_info']
        bearing_method = request.form['bearing_method']
        version = request.form['version']
        public_date = request.form['public_date']
        addi_block_type = request.form['addi_block_type']
        addi_block_desc = request.form['addi_block_desc']
        sound_id = request.form['sound_id']
        sound_content = request.form['sound_content']
        notes = request.form['notes']
        search_method = request.form['search_method']
        key_word = request.form['key_word']
        sum = request.form['sum']
        system = request.form['system']
        sound_chara = request.form['sound_chara']
        colors = request.form['colors']
        resolution = request.form['resolution']
        sound_qua = request.form['sound_qua']
        frame_qua = request.form['frame_qua']
        mode = request.form['mode']
        #type = request.form['type']
        depth = request.form['depth']
        video_sampling_frequency = request.form['video_sampling_frequency']
        language_id = request.form['language_id']
        language_type = request.form['language_type']
        subtitle_id = request.form['subtitle_id']
        subtitle_type = request.form['subtitle_type']
        audience = request.form['audience']
        ori_form = request.form['ori_form']
        other_form = request.form['other_form']
        inclusion = request.form['inclusion']
        included = request.form['included']
        refering = request.form['refering']
        reference = request.form['reference']
        copyright_holder = request.form['copyright_holder']
        copyright_notice = request.form['copyright_notice']
        authorize_person = request.form['authorize_person']
        authorize_form = request.form['authorize_form']
        authorize_date = request.form['authorize_date']
        authorize_due = request.form['authorize_due']
        authorize_area = request.form['authorize_area']
        authorize_file = request.form['authorize_file']
        authorize_info = request.form['authorize_info']
        time_length = request.form['time_length']
        space_length = request.form['space_length']
        source_carrier = request.form['source_carrier']
        collect_area = request.form['collect_area']
        collect_unit = request.form['collect_unit']
        call_number = request.form['call_number']
        collect_person = request.form['collect_person']
        process_unit = request.form['process_unit']
        serve_form = request.form['serve_form']
        serve_column = request.form['serve_column']
        serve_time = request.form['serve_time']
        serve_addr = request.form['serve_addr']
        serve_obj = request.form['serve_obj']
        acce_time = request.form['acce_time']
        acce_form = request.form['acce_form']
        acce_person = request.form['acce_person']
        acce_opi = request.form['acce_opi']
        acce_repo = request.form['acce_repo']
        episode = request.form['episode']
        total_episodes = request.form['total_episodes']
        producer = request.form['producer']
        pro_loca = request.form['pro_loca']
        resource = request.form['resource']
        provider = request.form['provider']
        video_date = request.form['video_date']
        #create_date = request.form['create_date']
        release_date = request.form['release_date']
        award = request.form['award']
        performance_form = request.form['performance_form']
        program_type = request.form['program_type']
        subtitle = request.form['subtitle']
        length = request.form['length']
        aspect_ratio = request.form['aspect_ratio']
        bit_rate = request.form['bit_rate']
        sound_track = request.form['sound_track']
        data_rate = request.form['data_rate']
        total_bitrate = request.form['total_bitrate']
        audio_sampling_frequency = request.form['audio_sampling_frequency']
        #size = request.form['size']
        #pattern = re.compile(r'(\d{4}-\d{1,2}-\d{1,2})')
        #match = pattern.match(create_date)
        #if match:
        if (title != 'None'):
            v.title = title
        #if (URL != 'None'):
        #    v.URL = URL
        if (parallel_title != 'None'):
            v.parallel_title = parallel_title
        if (alternate_title != 'None'):
            v.alternate_title = alternate_title
        if (other_title_info != 'None'):
            v.other_title_info = other_title_info
        if (series_title != 'None'):
            v.series_title = series_title
        if (parallel_series_title != 'None'):
            v.parallel_series_title = parallel_series_title
        if (individual_name != 'None'):
            v.individual_name = individual_name
        if (group_name != 'None'):
            v.group_name = group_name
        if (conference_name != 'None'):
            v.conference_name = conference_name
        if (joint_author_name != 'None'):
            v.joint_author_name = joint_author_name
        if (other_info != 'None'):
            v.other_info = other_info
        if (bearing_method != 'None'):
            v.bearing_method = bearing_method
        if (version != 'None'):
            v.version = version
        if (public_date != 'None'):
            v.public_date = public_date
        if (addi_block_type != 'None'):
            v.addi_block_type = addi_block_type
        if (addi_block_desc != 'None'):
            v.addi_block_desc = addi_block_desc
        if (sound_id != 'None'):
            v.sound_id = sound_id
        if (sound_content != 'None'):
            v.sound_content = sound_content
        if (notes != 'None'):
            v.notes = notes
        if (search_method != 'None'):
            v.search_method = search_method
        if (key_word != 'None'):
            v.key_word = key_word
        if (sum != 'None'):
            v.sum = sum
        if (system != 'None'):
            v.system = system
        if (sound_chara != 'None'):
            v.sound_chara = sound_chara
        if (colors != 'None'):
            v.colors = colors
        if (resolution != 'None'):
            v.resolution = resolution
        if (sound_qua != 'None'):
            v.sound_qua = sound_qua
        if (frame_qua != 'None'):
            v.frame_qua = frame_qua
        if (mode != 'None'):
            v.mode = mode
        #if (type != 'None'):
        #    v.type = type
        if (depth != 'None'):
            v.depth = depth
        if (video_sampling_frequency != 'None'):
            v.video_sampling_frequency = video_sampling_frequency
        if (language_id != 'None'):
            v.language_id = language_id
        if (language_type != 'None'):
            v.language_type = language_type
        if (subtitle_id != 'None'):
            v.subtitle_id = subtitle_id
        if (subtitle_type != 'None'):
            v.subtitle_type = subtitle_type
        if (audience != 'None'):
            v.audience = audience
        if (ori_form != 'None'):
            v.ori_form = ori_form
        if (other_form != 'None'):
            v.other_form = other_form
        if (inclusion != 'None'):
            v.inclusion = inclusion
        if (included != 'None'):
            v.included = included
        if (refering != 'None'):
            v.refering = refering
        if (reference != 'None'):
            v.reference = reference
        if (copyright_holder != 'None'):
            v.copyright_holder = copyright_holder
        if (copyright_notice != 'None'):
            v.copyright_notice = copyright_notice
        if (authorize_person != 'None'):
            v.authorize_person = authorize_person
        if (authorize_form != 'None'):
            v.authorize_form = authorize_form
        if (authorize_date != 'None'):
            v.authorize_date = authorize_date
        if (authorize_due != 'None'):
            v.authorize_due = authorize_due
        if (authorize_area != 'None'):
            v.authorize_area = authorize_area
        if (authorize_file != 'None'):
            v.authorize_file = authorize_file
        if (authorize_info != 'None'):
            v.authorize_info = authorize_info
        if (time_length != 'None'):
            v.time_length = time_length
        if (space_length != 'None'):
            v.space_length = space_length
        if (source_carrier != 'None'):
            v.source_carrier = source_carrier
        if (collect_area != 'None'):
            v.collect_area = collect_area
        if (collect_unit != 'None'):
            v.collect_unit = collect_unit
        if (call_number != 'None'):
            v.call_number = call_number
        if (collect_person != 'None'):
            v.collect_person = collect_person
        if (process_unit != 'None'):
            v.process_unit = process_unit
        if (serve_form != 'None'):
            v.serve_form = serve_form
        if (serve_column != 'None'):
            v.serve_column = serve_column
        if (serve_time != 'None'):
            v.serve_time = serve_time
        if (serve_addr != 'None'):
            v.serve_addr = serve_addr
        if (serve_obj != 'None'):
            v.serve_obj = serve_obj
        if (acce_time != 'None'):
            v.acce_time = acce_time
        if (acce_form != 'None'):
            v.acce_form = acce_form
        if (acce_person != 'None'):
            v.acce_person = acce_person
        if (acce_opi != 'None'):
            v.acce_opi = acce_opi
        if (acce_repo != 'None'):
            v.acce_repo = acce_repo
        if (episode != 'None'):
            v.episode = episode
        if (total_episodes != 'None'):
            v.total_episodes = total_episodes
        if (producer != 'None'):
            v.producer = producer
        if (pro_loca != 'None'):
            v.pro_loca = pro_loca
        if (resource != 'None'):
            v.resource = resource
        if (provider != 'None'):
            v.provider = provider
        if (video_date != 'None'):
            v.video_date = video_date
        #if (create_date != 'None'):
        #    v.create_date = create_date
        if (release_date != 'None'):
            v.release_date = release_date
        if (award != 'None'):
            v.award = award
        if (performance_form != 'None'):
            v.performance_form = performance_form
        if (program_type != 'None'):
            v.program_type = program_type
        if (subtitle != 'None'):
            v.subtitle = subtitle
        if (length != 'None'):
            v.length = length
        if (aspect_ratio != 'None'):
            v.aspect_ratio = aspect_ratio
        if (bit_rate != 'None'):
            v.bit_rate = bit_rate
        if (sound_track != 'None'):
            v.sound_track = sound_track
        if (data_rate != 'None'):
            v.data_rate = data_rate
        if (total_bitrate != 'None'):
            v.total_bitrate = total_bitrate
        if (audio_sampling_frequency != 'None'):
            v.audio_sampling_frequency = audio_sampling_frequency
        #if (size != 'None'):
        #    v.size = size
        create_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        v.create_date = create_date
        db.session.commit()  # 提交数据库会话
        flash('Item updated.')
        return redirect(url_for('index'))  # 重定向回主页
    #else:
    #    flash('Date format error.')
    #   return render_template('editvideo.html', videos=v)

    return render_template('editvideo.html', videos=v)

@app.route('/editrecord<int:record_id>', methods=['GET', 'POST'])
@login_required
def editrecord(record_id):
    r = Records.query.get_or_404(record_id)
    if request.method == 'POST': # 处理编辑表单的提交请求
        title = request.form['title']
        #URL = request.form['URL']
        pro_loca = request.form['pro_loca']
        provider = request.form['provider']
        record_date = request.form['record_date']
        release_date = request.form['release_date']
        singing_form = request.form['singing_form']
        sound_track = request.form['sound_track']
        #size = request.form['size']
        length = request.form['length']
        bit_rate = request.form['bit_rate']
        #type = request.form['type']
        mode = request.form['mode']
        alternate_title = request.form['alternate_title']
        other_title_info = request.form['other_title_info']
        series_title = request.form['series_title']
        parallel_series_title = request.form['parallel_series_title']
        total_episodes = request.form['total_episodes']
        episode = request.form['episode']
        individual_name = request.form['individual_name']
        group_name = request.form['group_name']
        conference_name = request.form['conference_name']
        joint_author_name = request.form['joint_author_name']
        other_info = request.form['other_info']
        bearing_method = request.form['bearing_method']
        version = request.form['version']
        producer = request.form['producer']
        public_date = request.form['public_date']
        award = request.form['award']
        singing_style = request.form['singing_style']
        parts = request.form['parts']
        perform_form = request.form['perform_form']
        notes = request.form['notes']
        search_method = request.form['search_method']
        key_word = request.form['key_word']
        perf_type = request.form['perf_type']
        perf_form = request.form['perf_form']
        sum = request.form['sum']
        mesh_point = request.form['mesh_point']
        audio_sampling_frequency = request.form['audio_sampling_frequency']
        depth = request.form['depth']
        language_id = request.form['language_id']
        language_type = request.form['language_type']
        audience = request.form['audience']
        resource = request.form['resource']
        ori_form = request.form['ori_form']
        other_form = request.form['other_form']
        inclusion = request.form['inclusion']
        included = request.form['included']
        referring = request.form['referring']
        reference = request.form['reference']
        copyright_holder = request.form['copyright_holder']
        copyright_notice = request.form['copyright_notice']
        authorize_person = request.form['authorize_person']
        authorize_form = request.form['authorize_form']
        authorize_date = request.form['authorize_date']
        authorize_due = request.form['authorize_due']
        authorize_area = request.form['authorize_area']
        authorize_file = request.form['authorize_file']
        authorize_info = request.form['authorize_info']
        time_length = request.form['time_length']
        space_length = request.form['space_length']
        source_carrier = request.form['source_carrier']
        collect_person = request.form['collect_person']
        process_unit = request.form['process_unit']
        serve_form = request.form['serve_form']
        serve_column = request.form['serve_column']
        serve_time = request.form['serve_time']
        serve_addr = request.form['serve_addr']
        serve_obj = request.form['serve_obj']
        acce_time = request.form['acce_time']
        acce_form = request.form['acce_form']
        acce_person = request.form['acce_person']
        acce_opi = request.form['acce_opi']
        acce_repo = request.form['acce_repo']
        if (title != 'None'):
            r.title = title  # 更新标题
        #if (URL != 'None'):
        #    r.URL = URL
        if (pro_loca != 'None'):
            r.pro_loca = pro_loca
        if (provider != 'None'):
            r.provider = provider
        if (record_date != 'None'):
            r.record_date = record_date
        create_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        r.create_date = create_date
        if (release_date != 'None'):
            r.release_date = release_date
        if (singing_form != 'None'):
            r.singing_form = singing_form
        if (sound_track != 'None'):
            r.sound_track = sound_track
        #if (size != 'None'):
        #    r.size = size
        if (length != 'None'):
            r.length = length
        if (bit_rate != 'None'):
            r.bit_rate = bit_rate
        #if (type != 'None'):
        #    r.type = type
        if (mode != 'None'):
            r.mode = mode
        if (alternate_title != 'None'):
            r.alternate_title = alternate_title
        if (other_title_info != 'None'):
            r.other_title_info = other_title_info
        if (series_title != 'None'):
            r.series_title = series_title
        if (parallel_series_title != 'None'):
            r.parallel_series_title = parallel_series_title
        if (total_episodes != 'None'):
            r.total_episodes = total_episodes
        if (episode != 'None'):
            r.episode = episode
        if (individual_name != 'None'):
            r.individual_name = individual_name
        if (group_name != 'None'):
            r.group_name = group_name
        if (conference_name != 'None'):
            r.conference_name = conference_name
        if (joint_author_name != 'None'):
            r.joint_author_name = joint_author_name
        if (other_info != 'None'):
            r.other_info = other_info
        if (bearing_method != 'None'):
            r.bearing_method = bearing_method
        if (version != 'None'):
            r.version = version
        if (producer != 'None'):
            r.producer = producer
        if (public_date != 'None'):
            r.public_date = public_date
        if (award != 'None'):
            r.award = award
        if (singing_style != 'None'):
            r.singing_style = singing_style
        if (parts != 'None'):
            r.parts = parts
        if (perform_form != 'None'):
            r.perform_form = perform_form
        if (notes != 'None'):
            r.notes = notes
        if (search_method != 'None'):
            r.search_method = search_method
        if (key_word != 'None'):
            r.key_word = key_word
        if (perf_type != 'None'):
            r.perf_type = perf_type
        if (perf_form != 'None'):
            r.perf_form = perf_form
        if (sum != 'None'):
            r.sum = sum
        if (mesh_point != 'None'):
            r.mesh_point = mesh_point
        if (audio_sampling_frequency != 'None'):
            r.audio_sampling_frequency = audio_sampling_frequency
        if (depth != 'None'):
            r.depth = depth
        if (language_id != 'None'):
            r.language_id = language_id
        if (language_type != 'None'):
            r.language_type = language_type
        if (audience != 'None'):
            r.audience = audience
        if (resource != 'None'):
            r.resource = resource
        if (ori_form != 'None'):
            r.ori_form = ori_form
        if (other_form != 'None'):
            r.other_form = other_form
        if (inclusion != 'None'):
            r.inclusion = inclusion
        if (included != 'None'):
            r.included = included
        if (referring != 'None'):
            r.referring = referring
        if (reference != 'None'):
            r.reference = reference
        if (copyright_holder != 'None'):
            r.copyright_holder = copyright_holder
        if (copyright_notice != 'None'):
            r.copyright_notice = copyright_notice
        if (authorize_person != 'None'):
            r.authorize_person = authorize_person
        if (authorize_form != 'None'):
            r.authorize_form = authorize_form
        if (authorize_date != 'None'):
            r.authorize_date = authorize_date
        if (authorize_due != 'None'):
            r.authorize_due = authorize_due
        if (authorize_area != 'None'):
            r.authorize_area = authorize_area
        if (authorize_file != 'None'):
            r.authorize_file = authorize_file
        if (authorize_info != 'None'):
            r.authorize_info = authorize_info
        if (time_length != 'None'):
            r.time_length = time_length
        if (space_length != 'None'):
            r.space_length = space_length
        if (source_carrier != 'None'):
            r.source_carrier = source_carrier
        if (collect_person != 'None'):
            r.collect_person = collect_person
        if (process_unit != 'None'):
            r.process_unit = process_unit
        if (serve_form != 'None'):
            r.serve_form = serve_form
        if (serve_column != 'None'):
            r.serve_column = serve_column
        if (serve_time != 'None'):
            r.serve_time = serve_time
        if (serve_addr != 'None'):
            r.serve_addr = serve_addr
        if (serve_obj != 'None'):
            r.serve_obj = serve_obj
        if (acce_time != 'None'):
            r.acce_time = acce_time
        if (acce_form != 'None'):
            r.acce_form = acce_form
        if (acce_person != 'None'):
            r.acce_person = acce_person
        if (acce_opi != 'None'):
            r.acce_opi = acce_opi
        if (acce_repo != 'None'):
            r.acce_repo = acce_repo

        db.session.commit()  # 提交数据库会话
        flash('Item updated.')
        return redirect(url_for('index'))  # 重定向回主页
    return render_template('editrecord.html', records=r)


@app.route('/editdocument<int:document_id>', methods=['GET', 'POST'])
@login_required
def editdocument(document_id):
    r = Documents.query.get_or_404(document_id)
    if request.method == 'POST': # 处理编辑表单的提交请求
        title = request.form['title']
        parallel_title = request.form['parallel_title']
        alternate_title = request.form['alternate_title']
        other_title_info = request.form['other_title_info']
        individual_name = request.form['individual_name']
        group_name = request.form['group_name']
        conference_name = request.form['conference_name']
        joint_author_name = request.form['joint_author_name']
        other_info = request.form['other_info']
        bearing_method = request.form['bearing_method']
        version = request.form['version']
        pro_loca = request.form['pro_loca']
        producer = request.form['producer']
        public_date = request.form['public_date']
        release_date = request.form['release_date']
        abstract = request.form['abstract']
        catalog = request.form['catalog']
        award = request.form['award']
        notes = request.form['notes']
        search_method = request.form['search_method']
        key_word = request.form['key_word']
        sum = request.form['sum']
        #type = request.form['type']
        audience = request.form['audience']
        resource = request.form['resource']
        provider = request.form['provider']
        inclusion = request.form['inclusion']
        included = request.form['included']
        copyright_holder = request.form['copyright_holder']
        copyright_notice = request.form['copyright_notice']
        authorize_person = request.form['authorize_person']
        authorize_form = request.form['authorize_form']
        authorize_date = request.form['authorize_date']
        authorize_due = request.form['authorize_due']
        authorize_area = request.form['authorize_area']
        authorize_file = request.form['authorize_file']
        authorize_info = request.form['authorize_info']
        time_length = request.form['time_length']
        space_length = request.form['space_length']
        source_carrier = request.form['source_carrier']
        collect_area = request.form['collect_area']
        collect_unit = request.form['collect_unit']
        call_number = request.form['call_number']
        collect_person = request.form['collect_person']
        process_unit = request.form['process_unit']
        serve_form = request.form['serve_form']
        serve_column = request.form['serve_column']
        serve_time = request.form['serve_time']
        serve_addr = request.form['serve_addr']
        serve_obj = request.form['serve_obj']
        acce_time = request.form['acce_time']
        acce_form = request.form['acce_form']
        acce_person = request.form['acce_person']
        acce_opi = request.form['acce_opi']
        acce_repo = request.form['acce_repo']
        if (title != 'None'):
            r.title = title  # 更新标题
        if (parallel_title != 'None'):
            r.parallel_title=parallel_title
        if (alternate_title != 'None'):
            r.alternate_title=alternate_title
        if (other_title_info != 'None'):
            r.other_title_info=other_title_info
        if (individual_name != 'None'):
            r.individual_name=individual_name
        if (group_name != 'None'):
            r.group_name=group_name
        if (conference_name != 'None'):
            r.conference_name=conference_name
        if (joint_author_name != 'None'):
            r.joint_author_name=joint_author_name
        if (other_info != 'None'):
            r.other_info=other_info
        if (bearing_method != 'None'):
            r.bearing_method=bearing_method
        if (version != 'None'):
            r.version=version
        if (pro_loca != 'None'):
            r.pro_loca=pro_loca
        if (producer != 'None'):
            r.producer=producer
        if (public_date != 'None'):
            r.public_date=public_date
        if (release_date != 'None'):
            r.release_date=release_date
        if (abstract != 'None'):
            r.abstract=abstract
        if (catalog != 'None'):
            r.catalog=catalog
        if (award != 'None'):
            r.award=award
        if (notes != 'None'):
            r.notes=notes
        if (search_method != 'None'):
            r.search_method=search_method
        if (key_word != 'None'):
            r.key_word=key_word
        if (sum != 'None'):
            r.sum=sum
        #if (type != 'None'):
         #   r.type=type
        if (audience != 'None'):
            r.audience=audience
        if (resource != 'None'):
            r.resource=resource
        if (provider != 'None'):
            r.provider=provider
        if (inclusion != 'None'):
            r.inclusion=inclusion
        if (included != 'None'):
            r.included=included
        if (copyright_holder != 'None'):
            r.copyright_holder=copyright_holder
        if (copyright_notice != 'None'):
            r.copyright_notice=copyright_notice
        if (authorize_person != 'None'):
            r.authorize_person=authorize_person
        if (authorize_form != 'None'):
            r.authorize_form=authorize_form
        if (authorize_date != 'None'):
            r.authorize_date=authorize_date
        if (authorize_due != 'None'):
            r.authorize_due=authorize_due
        if (authorize_area != 'None'):
            r.authorize_area=authorize_area
        if (authorize_file != 'None'):
            r.authorize_file=authorize_file
        if (authorize_info != 'None'):
            r.authorize_info=authorize_info
        if (time_length != 'None'):
            r.time_length=time_length
        if (space_length != 'None'):
            r.space_length=space_length
        if (source_carrier != 'None'):
            r.source_carrier=source_carrier
        if (collect_area != 'None'):
            r.collect_area=collect_area
        if (collect_unit != 'None'):
            r.collect_unit=collect_unit
        if (call_number != 'None'):
            r.call_number=call_number
        if (collect_person != 'None'):
            r.collect_person=collect_person
        if (process_unit != 'None'):
            r.process_unit=process_unit
        if (serve_form != 'None'):
            r.serve_form=serve_form
        if (serve_column != 'None'):
            r.serve_column=serve_column
        if (serve_time != 'None'):
            r.serve_time=serve_time
        if (serve_addr != 'None'):
            r.serve_addr=serve_addr
        if (serve_obj != 'None'):
            r.serve_obj=serve_obj
        if (acce_time != 'None'):
            r.acce_time=acce_time
        if (acce_form != 'None'):
            r.acce_form=acce_form
        if (acce_person != 'None'):
            r.acce_person=acce_person
        if (acce_opi != 'None'):
            r.acce_opi=acce_opi
        if (acce_repo != 'None'):
            r.acce_repo=acce_repo

        create_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        r.create_date = create_date
        db.session.commit()  # 提交数据库会话
        flash('Item updated.')
        return redirect(url_for('index'))  # 重定向回主页
    return render_template('editdocument.html', documents=r)


@app.route('/editpicture<int:picture_id>', methods=['GET', 'POST'])
@login_required
def editpicture(picture_id):
    pict = Pictures.query.get_or_404(picture_id)
    if request.method == 'POST': # 处理编辑表单的提交请求
        title = request.form['title']
        individual_name = request.form['individual_name']
        group_name = request.form['group_name']
        pro_loca = request.form['pro_loca']
        pic_date = request.form['pic_date']
        release_date = request.form['release_date']
        resolution = request.form['resolution']
        parallel_title = request.form['parallel_title']
        alternate_title = request.form['alternate_title']
        other_title_info = request.form['other_title_info']
        conference_name = request.form['conference_name']
        joint_author_name = request.form['joint_author_name']
        other_info = request.form['other_info']
        bearing_method = request.form['bearing_method']
        version = request.form['version']
        producer = request.form['producer']
        public_date = request.form['public_date']
        award = request.form['award']
        notes = request.form['notes']
        search_method = request.form['search_method']
        key_word = request.form['key_word']
        sum = request.form['sum']
        colors = request.form['colors']
        audience = request.form['audience']
        resource = request.form['resource']
        provider = request.form['provider']
        #type = request.form['type']
        inclusion = request.form['inclusion']
        included = request.form['included']
        copyright_holder = request.form['copyright_holder']
        copyright_notice = request.form['copyright_notice']
        authorize_person = request.form['authorize_person']
        authorize_form = request.form['authorize_form']
        authorize_date = request.form['authorize_date']
        authorize_due = request.form['authorize_due']
        authorize_area = request.form['authorize_area']
        authorize_file = request.form['authorize_file']
        authorize_info = request.form['authorize_info']
        time_length = request.form['time_length']
        space_length = request.form['space_length']
        source_carrier = request.form['source_carrier']
        collect_person = request.form['collect_person']
        process_unit = request.form['process_unit']
        serve_form = request.form['serve_form']
        serve_column = request.form['serve_column']
        serve_time = request.form['serve_time']
        serve_addr = request.form['serve_addr']
        serve_obj = request.form['serve_obj']
        acce_time = request.form['acce_time']
        acce_form = request.form['acce_form']
        acce_person = request.form['acce_person']
        acce_opi = request.form['acce_opi']
        acce_repo = request.form['acce_repo']
        if (title != 'None'):
            pict.title = title  # 更新标题
        create_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        pict.create_date = create_date
        if (individual_name!='None'):
            pict.individual_name=individual_name
        if (group_name != 'None'):
            pict.group_name=group_name
        if (pro_loca != 'None'):
            pict.pro_loca=pro_loca
        if (pic_date != 'None'):
            pict.pic_date=pic_date
        if (release_date != 'None'):
            pict.release_date=release_date
        if (resolution != 'None'):
            pict.resolution=resolution
        if (parallel_title != 'None'):
            pict.parallel_title=parallel_title
        if (alternate_title != 'None'):
            pict.alternate_title=alternate_title
        if (other_title_info != 'None'):
            pict.other_title_info=other_title_info
        if (conference_name != 'None'):
            pict.conference_name=conference_name
        if (joint_author_name != 'None'):
            pict.joint_auther_name=joint_author_name
        if (other_info != 'None'):
            pict.other_info=other_info
        if (bearing_method != 'None'):
            pict.bearing_method=bearing_method
        if (version != 'None'):
            pict.version=version
        if (producer != 'None'):
            pict.producer=producer
        if (public_date != 'None'):
            pict.public_date=public_date
        if (award != 'None'):
            pict.award=award
        if (notes != 'None'):
            pict.notes=notes
        if (search_method != 'None'):
            pict.search_method=search_method
        if (key_word != 'None'):
            pict.key_word=key_word
        if (sum != 'None'):
            pict.sum=sum
        if (colors != 'None'):
            pict.colors=colors
        if (audience != 'None'):
            pict.audience=audience
        if (resource != 'None'):
            pict.resource=resource
        if (provider != 'None'):
            pict.provider=provider
        #if (type != 'None'):
         #   pict.type=type
        if (inclusion != 'None'):
            pict.inclusion=inclusion
        if (included != 'None'):
            pict.included=included
        if (copyright_holder != 'None'):
            pict.copyright_holder=copyright_holder
        if (copyright_notice != 'None'):
            pict.copyright_notice=copyright_notice
        if (authorize_person != 'None'):
            pict.authorize_person=authorize_person
        if (authorize_form != 'None'):
            pict.authorize_form=authorize_form
        if (authorize_date != 'None'):
            pict.authorize_date=authorize_date
        if (authorize_due != 'None'):
            pict.authorize_due=authorize_due
        if (authorize_area != 'None'):
            pict.authorize_area=authorize_area
        if (authorize_file != 'None'):
            pict.authorize_file=authorize_file
        if (authorize_info != 'None'):
            pict.authorize_info=authorize_info
        if (time_length != 'None'):
            pict.time_length=time_length
        if (space_length != 'None'):
            pict.space_length=space_length
        if (source_carrier != 'None'):
            pict.source_carrier=source_carrier
        if (collect_person != 'None'):
            pict.collect_person=collect_person
        if (process_unit != 'None'):
            pict.process_unit=process_unit
        if (serve_form != 'None'):
            pict.serve_form=serve_form
        if (serve_column != 'None'):
            pict.serve_column=serve_column
        if (serve_time != 'None'):
            pict.serve_time=serve_time
        if (serve_addr != 'None'):
            pict.serve_addr=serve_addr
        if (serve_obj != 'None'):
            pict.serve_obj=serve_obj
        if (acce_time != 'None'):
            pict.acce_time=acce_time
        if (acce_form != 'None'):
            pict.acce_form=acce_form
        if (acce_person != 'None'):
            pict.acce_person=acce_person
        if (acce_opi != 'None'):
            pict.acce_opi=acce_opi
        if (acce_repo != 'None'):
            pict.acce_repo=acce_repo
        db.session.commit()  # 提交数据库会话
        flash('Item updated.')
        return redirect(url_for('index'))  # 重定向回主页
    return render_template('editpicture.html', pictures=pict)

@app.route('/addpicture', methods=['GET', 'POST'])
def addpicture():
    if request.method == 'POST':  # 处理编辑表单的提交请求
        title = request.form['title']
        individual_name = request.form['individual_name']
        group_name = request.form['group_name']
        pro_loca = request.form['pro_loca']
        pic_date = request.form['pic_date']
        release_date = request.form['release_date']
        resolution = request.form['resolution']
        parallel_title = request.form['parallel_title']
        alternate_title = request.form['alternate_title']
        other_title_info = request.form['other_title_info']
        conference_name = request.form['conference_name']
        joint_author_name = request.form['joint_author_name']
        other_info = request.form['other_info']
        bearing_method = request.form['bearing_method']
        version = request.form['version']
        producer = request.form['producer']
        public_date = request.form['public_date']
        award = request.form['award']
        notes = request.form['notes']
        search_method = request.form['search_method']
        key_word = request.form['key_word']
        sum = request.form['sum']
        colors = request.form['colors']
        audience = request.form['audience']
        resource = request.form['resource']
        provider = request.form['provider']
        #type = request.form['type']
        inclusion = request.form['inclusion']
        included = request.form['included']
        copyright_holder = request.form['copyright_holder']
        copyright_notice = request.form['copyright_notice']
        authorize_person = request.form['authorize_person']
        authorize_form = request.form['authorize_form']
        authorize_date = request.form['authorize_date']
        authorize_due = request.form['authorize_due']
        authorize_area = request.form['authorize_area']
        authorize_file = request.form['authorize_file']
        authorize_info = request.form['authorize_info']
        time_length = request.form['time_length']
        space_length = request.form['space_length']
        source_carrier = request.form['source_carrier']
        collect_person = request.form['collect_person']
        process_unit = request.form['process_unit']
        serve_form = request.form['serve_form']
        serve_column = request.form['serve_column']
        serve_time = request.form['serve_time']
        serve_addr = request.form['serve_addr']
        serve_obj = request.form['serve_obj']
        acce_time = request.form['acce_time']
        acce_form = request.form['acce_form']
        acce_person = request.form['acce_person']
        acce_opi = request.form['acce_opi']
        acce_repo = request.form['acce_repo']
        fname = request.files['img']  # 获取上传的文件
        fname1 = request.files['img']
        pattern1 = re.compile(r'(.*\.jpg)')
        match1 = pattern1.match(fname.filename)
        if match1 :
            hou='.jpg'
        pattern2 = re.compile(r'(.*\.gif)')
        match2 = pattern2.match(fname.filename)
        if match2 :
            hou='.gif'
        pattern3 = re.compile(r'(.*\.bmp)')
        match3 = pattern3.match(fname.filename)
        if match3 :
            hou='.bmp'
        pattern4 = re.compile(r'(.*\.png)')
        match4 = pattern4.match(fname.filename)
        if match4 :
            hou='.png'
        strr=time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        if (match1 or match2 or match3 or match4):
            new_fname = r'watchlist/static/resource/pictures/' + strr + hou
            fname.save(new_fname)  # 保存文件到指定路径
            f = open(new_fname, "rb")
            strx = int(len(f.read()))
            strx = strx/1024
            if (strx > 1024):
                str2 = strx / 1024
                str2 = round(str2, 1)
                str1 = str(str2) + 'mb'
            else:
                if (strx%1==0):
                    strx = int(strx)
                    str1 = str(strx) + 'kb'
                else:
                    strx=round(strx, 1)
                    str1 = str(strx) + 'kb'
            flash('Item created.')  # 显示成功创建的提示
            create_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            pict = Pictures(title=title, URL='resource/Pictures/'+strr+hou, individual_name=individual_name,group_name=group_name, pro_loca=pro_loca,pic_date=pic_date, create_date=create_date, release_date=release_date, size=str1,
                resolution=resolution,parallel_title=parallel_title,alternate_title=alternate_title,other_title_info=other_title_info,conference_name =conference_name,joint_author_name =joint_author_name,other_info=other_info,
                bearing_method=bearing_method,version=version,producer=producer,public_date=public_date,award=award,notes=notes,search_method=search_method,key_word=key_word,sum=sum,colors=colors,audience=audience,resource=resource,
                provider =provider,type=hou,inclusion=inclusion,included=included,copyright_holder=copyright_holder,copyright_notice=copyright_notice,authorize_person=authorize_person,authorize_form=authorize_form,authorize_date=authorize_date,authorize_due=authorize_due,authorize_area=authorize_area,
                authorize_file=authorize_file,authorize_info=authorize_info,time_length=time_length,space_length=space_length,source_carrier=source_carrier,collect_person=collect_person,process_unit=process_unit,serve_form=serve_form,
                serve_column=serve_column,serve_time=serve_time,serve_addr=serve_addr,serve_obj=serve_obj,acce_time=acce_time,acce_form=acce_form,acce_person=acce_person,acce_opi=acce_opi,acce_repo=acce_repo)  # 创建记录
            db.session.add(pict)  # 添加到数据库会话
            db.session.commit()  # 提交数据库会
            user = User.query.first()  # 读取用户记录
            pics = Pictures.query.order_by(Pictures.create_date.desc()).all()  # 图片
            return render_template('indexpicture.html', user=user, pictures=pics)
        else:
            flash('Date format error.')
            return render_template('addpicture.html')
    return render_template('addpicture.html')

@app.route('/adddocument', methods=['GET', 'POST'])
def adddocument():
    if request.method == 'POST': # 处理编辑表单的提交请求
        parallel_title=request.form['parallel_title']
        alternate_title=request.form['alternate_title']
        other_title_info=request.form['other_title_info']
        individual_name=request.form['individual_name']
        group_name=request.form['group_name']
        conference_name=request.form['conference_name']
        joint_author_name=request.form['joint_author_name']
        other_info=request.form['other_info']
        bearing_method=request.form['bearing_method']
        version=request.form['version']
        pro_loca=request.form['pro_loca']
        producer=request.form['producer']
        public_date=request.form['public_date']
        release_date=request.form['release_date']
        abstract=request.form['abstract']
        catalog=request.form['catalog']
        award=request.form['award']
        notes=request.form['notes']
        search_method=request.form['search_method']
        key_word=request.form['key_word']
        sum=request.form['sum']
        #type=request.form['type']
        audience=request.form['audience']
        resource=request.form['resource']
        provider=request.form['provider']
        inclusion=request.form['inclusion']
        included=request.form['included']
        copyright_holder=request.form['copyright_holder']
        copyright_notice=request.form['copyright_notice']
        authorize_person=request.form['authorize_person']
        authorize_form=request.form['authorize_form']
        authorize_date=request.form['authorize_date']
        authorize_due=request.form['authorize_due']
        authorize_area=request.form['authorize_area']
        authorize_file=request.form['authorize_file']
        authorize_info=request.form['authorize_info']
        time_length=request.form['time_length']
        space_length=request.form['space_length']
        source_carrier=request.form['source_carrier']
        collect_area=request.form['collect_area']
        collect_unit=request.form['collect_unit']
        call_number=request.form['call_number']
        collect_person=request.form['collect_person']
        process_unit=request.form['process_unit']
        serve_form=request.form['serve_form']
        serve_column=request.form['serve_column']
        serve_time=request.form['serve_time']
        serve_addr=request.form['serve_addr']
        serve_obj=request.form['serve_obj']
        acce_time=request.form['acce_time']
        acce_form=request.form['acce_form']
        acce_person=request.form['acce_person']
        acce_opi=request.form['acce_opi']
        acce_repo=request.form['acce_repo']
        title = request.form['title']
        fname = request.files['img']  # 获取上传的文件
        pattern1 = re.compile(r'(.*\.txt)')
        match1 = pattern1.match(fname.filename)
        if match1 :
            hou='.txt'
        pattern2 = re.compile(r'(.*\.pdf)')
        match2 = pattern2.match(fname.filename)
        if match2 :
            hou='.pdf'
        pattern3 = re.compile(r'(.*\.html)')
        match3 = pattern3.match(fname.filename)
        if match3 :
            hou='.html'
        pattern5 = re.compile(r'(.*\.docx)')
        match5 = pattern5.match(fname.filename)
        if match5:
            hou = '.docx'
        pattern6 = re.compile(r'(.*\.htl)')
        match6 = pattern6.match(fname.filename)
        if match6:
            hou = '.htl'
        pattern7 = re.compile(r'(.*\.doc)')
        match7 = pattern7.match(fname.filename)
        if match7:
            hou = '.doc'
        pattern8 = re.compile(r'(.*\.epub)')
        match8 = pattern8.match(fname.filename)
        if match8:
            hou = '.epub'
        pattern9 = re.compile(r'(.*\.mobi)')
        match9 = pattern9.match(fname.filename)
        if match9:
            hou = '.mobi'
        pattern10 = re.compile(r'(.*\.azw)')
        match10 = pattern10.match(fname.filename)
        if match10:
            hou = '.azw'
        strr=time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        if (match1 or match2 or match3 or match5 or match6 or match7 or match8 or match9 or match10):
            new_fname = r'watchlist/static/resource/documents/' + strr + hou
            fname.save(new_fname)  # 保存文件到指定路径
            f = open(new_fname, "rb")
            strx = int(len(f.read()))
            strx = strx/1024
            if (strx > 1024):
                str2 = strx / 1024
                str2 = round(str2, 1)
                str1 = str(str2) + 'mb'
            else:
                if (strx%1==0):
                    strx = int(strx)
                    str1 = str(strx) + 'kb'
                else:
                    strx=round(strx, 1)
                    str1 = str(strx) + 'kb'
            flash('Item created.')  # 显示成功创建的提示
            create_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            pict = Documents(title=title, URL='resource/documents/'+strr+hou,size=str1,create_date=create_date,parallel_title=parallel_title,alternate_title=alternate_title,other_title_info=other_title_info,individual_name=individual_name,group_name=group_name,conference_name=conference_name,joint_author_name=joint_author_name,other_info=other_info,bearing_method=bearing_method,
                version=version,pro_loca=pro_loca,producer=producer,public_date=public_date,release_date=release_date,abstract=abstract,catalog=catalog,award=award,notes=notes,search_method=search_method,key_word=key_word,sum=sum,type=hou,audience=audience,resource=resource,provider=provider,inclusion=inclusion,included=included,
                copyright_holder=copyright_holder,copyright_notice=copyright_notice,authorize_person=authorize_person,authorize_form=authorize_form,authorize_date=authorize_date,authorize_due=authorize_due,authorize_area=authorize_area,authorize_file=authorize_file,authorize_info=authorize_info,time_length=time_length,space_length=space_length,
                source_carrier=source_carrier,collect_area=collect_area,collect_unit=collect_unit,call_number=call_number,collect_person=collect_person,process_unit=process_unit,serve_form=serve_form,serve_column=serve_column,serve_time=serve_time,serve_addr=serve_addr,serve_obj=serve_obj,acce_time=acce_time,acce_form=acce_form,acce_person=acce_person,acce_opi=acce_opi,acce_repo=acce_repo)  # 创建记录
            db.session.add(pict)  # 添加到数据库会
            db.session.commit()  # 提交数据库会
            user = User.query.first()  # 读取用户记录
            docs = Documents.query.order_by(Documents.create_date.desc()).all()  # 图片
            return render_template('indexdocument.html', user=user, documents=docs)
        else:
            flash('Date format error.')
            return render_template('adddocument.html')
    return render_template('adddocument.html')

@app.route('/addrecord', methods=['GET', 'POST'])
def addrecord():
    if request.method == 'POST': # 处理编辑表单的提交请求
        title = request.form['title']
        pro_loca = request.form['pro_loca']
        provider = request.form['provider']
        record_date = request.form['record_date']
        release_date = request.form['release_date']
        singing_form = request.form['singing_form']
        sound_track = request.form['sound_track']
        length = request.form['length']
        bit_rate = request.form['bit_rate']
        #type = request.form['type']
        mode = request.form['mode']
        alternate_title = request.form['alternate_title']
        other_title_info = request.form['other_title_info']
        series_title = request.form['series_title']
        parallel_series_title = request.form['parallel_series_title']
        total_episodes = request.form['total_episodes']
        episode = request.form['episode']
        individual_name = request.form['individual_name']
        group_name = request.form['group_name']
        conference_name = request.form['conference_name']
        joint_author_name = request.form['joint_author_name']
        other_info = request.form['other_info']
        bearing_method = request.form['bearing_method']
        version = request.form['version']
        producer = request.form['producer']
        public_date = request.form['public_date']
        award = request.form['award']
        singing_style = request.form['singing_style']
        parts = request.form['parts']
        perform_form = request.form['perform_form']
        notes = request.form['notes']
        search_method = request.form['search_method']
        key_word = request.form['key_word']
        perf_type = request.form['perf_type']
        perf_form = request.form['perf_form']
        sum = request.form['sum']
        mesh_point = request.form['mesh_point']
        audio_sampling_frequency = request.form['audio_sampling_frequency']
        depth = request.form['depth']
        language_id = request.form['language_id']
        language_type = request.form['language_type']
        audience = request.form['audience']
        resource = request.form['resource']
        ori_form = request.form['ori_form']
        other_form = request.form['other_form']
        inclusion = request.form['inclusion']
        included = request.form['included']
        referring = request.form['referring']
        reference = request.form['reference']
        copyright_holder = request.form['copyright_holder']
        copyright_notice = request.form['copyright_notice']
        authorize_person = request.form['authorize_person']
        authorize_form = request.form['authorize_form']
        authorize_date = request.form['authorize_date']
        authorize_due = request.form['authorize_due']
        authorize_area = request.form['authorize_area']
        authorize_file = request.form['authorize_file']
        authorize_info = request.form['authorize_info']
        time_length = request.form['time_length']
        space_length = request.form['space_length']
        source_carrier = request.form['source_carrier']
        collect_person = request.form['collect_person']
        process_unit = request.form['process_unit']
        serve_form = request.form['serve_form']
        serve_column = request.form['serve_column']
        serve_time = request.form['serve_time']
        serve_addr = request.form['serve_addr']
        serve_obj = request.form['serve_obj']
        acce_time = request.form['acce_time']
        acce_form = request.form['acce_form']
        acce_person = request.form['acce_person']
        acce_opi = request.form['acce_opi']
        acce_repo = request.form['acce_repo']
        fname = request.files['img']  # 获取上传的文件
        pattern1 = re.compile(r'(.*\.mp3)')
        match1 = pattern1.match(fname.filename)
        if match1:
            hou='.mp3'
        pattern2 = re.compile(r'(.*\.wma)')
        match2 = pattern2.match(fname.filename)
        if match2:
            hou='.wma'
        pattern3 = re.compile(r'(.*\.wav)')
        match3 = pattern3.match(fname.filename)
        if match3:
            hou='.wav'
        pattern4 = re.compile(r'(.*\.qpe)')
        match4 = pattern4.match(fname.filename)
        if match4:
            hou='.qpe'
        pattern5 = re.compile(r'(.*\.aac)')
        match5 = pattern5.match(fname.filename)
        if match5:
            hou='.aac'
        pattern6 = re.compile(r'(.*\.mflac)')
        match6 = pattern6.match(fname.filename)
        if match6:
            hou = '.mflac'
        pattern7 = re.compile(r'(.*\.flac)')
        match7 = pattern7.match(fname.filename)
        if match7:
            hou = '.flac'
        strr= time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        if (match1 or match2 or match3 or match4 or match5 or match6 or match7):
            new_fname = r'watchlist/static/resource/musics/' + strr + hou
            fname.save(new_fname)  # 保存文件到指定路径
            f = open(new_fname, "rb")
            strx = int(len(f.read()))
            strx = strx/1024
            if (strx > 1024):
                str2 = strx / 1024
                str2 = round(str2, 1)
                str1 = str(str2) + 'mb'
            else:
                if (strx%1==0):
                    strx = int(strx)
                    str1 = str(strx) + 'kb'
                else:
                    strx=round(strx, 1)
                    str1 = str(strx) + 'kb'
            flash('Item created.')  # 显示成功创建的提示
            create_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            reco = Records(title=title, URL='resource/musics/'+strr+hou, pro_loca=pro_loca, provider=provider,
                            record_date=record_date, create_date=create_date, release_date=release_date,
                            singing_form=singing_form, sound_track=sound_track, size=str1, length=length,
                            bit_rate=bit_rate, type=hou, mode=mode, alternate_title=alternate_title, other_title_info=other_title_info,
                            series_title=series_title, parallel_series_title=parallel_series_title, total_episodes=total_episodes,
                            episode=episode, individual_name=individual_name, group_name=group_name, conference_name=conference_name,
                            joint_author_name=joint_author_name, other_info=other_info, bearing_method=bearing_method, version=version,
                            producer=producer, public_date=public_date, award=award, singing_style=singing_style, parts=parts, perform_form=perform_form,
                            notes=notes, search_method=search_method, key_word=key_word, perf_type=perf_type, perf_form=perf_form, sum=sum, mesh_point=mesh_point,
                            audio_sampling_frequency=audio_sampling_frequency, depth=depth, language_id=language_id, language_type=language_type,
                            audience=audience, resource=resource, ori_form=ori_form, other_form=other_form, inclusion=inclusion,
                            included=included, referring=referring, reference=reference, copyright_holder=copyright_holder,
                            copyright_notice=copyright_notice, authorize_person=authorize_person, authorize_form=authorize_form,
                            authorize_date=authorize_date, authorize_due=authorize_due, authorize_area=authorize_area,
                            authorize_file=authorize_file, authorize_info=authorize_info, time_length=time_length, space_length=space_length,
                            source_carrier=source_carrier, collect_person=collect_person, process_unit=process_unit, serve_form=serve_form,
                            serve_column=serve_column, serve_time=serve_time, serve_addr=serve_addr, serve_obj=serve_obj, acce_time=acce_time,
                                acce_form=acce_form, acce_person=acce_person, acce_opi=acce_opi, acce_repo=acce_repo)  # 创建记录
            db.session.add(reco)  # 添加到数据库会话
            db.session.commit()  # 提交数据库会话
            user = User.query.first()  # 读取用户记录
            res = Records.query.order_by(Records.create_date.desc()).all()  # 图片
            return render_template('indexmusic.html', user=user, musics=res)
        else:
            flash('Date format error.')
            return render_template('addrecord.html')
    return render_template('addrecord.html')

@app.route('/addvideo', methods=['GET', 'POST'])
def addvideo():
    if request.method == 'POST': # 处理编辑表单的提交请求
        title = request.form['title']
        series=request.form['series']
        parallel_title = request.form['parallel_title']
        alternate_title = request.form['alternate_title']
        other_title_info = request.form['other_title_info']
        series_title = request.form['series_title']
        parallel_series_title = request.form['parallel_series_title']
        individual_name = request.form['individual_name']
        group_name = request.form['group_name']
        conference_name = request.form['conference_name']
        joint_author_name = request.form['joint_author_name']
        other_info = request.form['other_info']
        bearing_method = request.form['bearing_method']
        version = request.form['version']
        public_date = request.form['public_date']
        addi_block_type = request.form['addi_block_type']
        addi_block_desc = request.form['addi_block_desc']
        sound_id = request.form['sound_id']
        sound_content = request.form['sound_content']
        notes = request.form['notes']
        search_method = request.form['search_method']
        key_word = request.form['key_word']
        sum = request.form['sum']
        system = request.form['system']
        sound_chara = request.form['sound_chara']
        colors = request.form['colors']
        resolution = request.form['resolution']
        sound_qua = request.form['sound_qua']
        frame_qua = request.form['frame_qua']
        mode = request.form['mode']
        #type = request.form['type']
        depth = request.form['depth']
        video_sampling_frequency = request.form['video_sampling_frequency']
        language_id = request.form['language_id']
        language_type = request.form['language_type']
        subtitle_id = request.form['subtitle_id']
        subtitle_type = request.form['subtitle_type']
        audience = request.form['audience']
        ori_form = request.form['ori_form']
        other_form = request.form['other_form']
        inclusion = request.form['inclusion']
        included = request.form['included']
        refering = request.form['refering']
        reference = request.form['reference']
        copyright_holder = request.form['copyright_holder']
        copyright_notice = request.form['copyright_notice']
        authorize_person = request.form['authorize_person']
        authorize_form = request.form['authorize_form']
        authorize_date = request.form['authorize_date']
        authorize_due = request.form['authorize_due']
        authorize_area = request.form['authorize_area']
        authorize_file = request.form['authorize_file']
        authorize_info = request.form['authorize_info']
        time_length = request.form['time_length']
        space_length = request.form['space_length']
        source_carrier = request.form['source_carrier']
        collect_area = request.form['collect_area']
        collect_unit = request.form['collect_unit']
        call_number = request.form['call_number']
        collect_person = request.form['collect_person']
        process_unit = request.form['process_unit']
        serve_form = request.form['serve_form']
        serve_column = request.form['serve_column']
        serve_time = request.form['serve_time']
        serve_addr = request.form['serve_addr']
        serve_obj = request.form['serve_obj']
        acce_time = request.form['acce_time']
        acce_form = request.form['acce_form']
        acce_person = request.form['acce_person']
        acce_opi = request.form['acce_opi']
        acce_repo = request.form['acce_repo']
        episode = request.form['episode']
        total_episodes = request.form['total_episodes']
        producer = request.form['producer']
        pro_loca = request.form['pro_loca']
        resource = request.form['resource']
        provider = request.form['provider']
        video_date = request.form['video_date']
        #create_date = request.form['create_date']
        release_date = request.form['release_date']
        award = request.form['award']
        performance_form = request.form['performance_form']
        program_type = request.form['program_type']
        subtitle = request.form['subtitle']
        length = request.form['length']
        aspect_ratio = request.form['aspect_ratio']
        bit_rate = request.form['bit_rate']
        sound_track = request.form['sound_track']
        data_rate = request.form['data_rate']
        total_bitrate = request.form['total_bitrate']
        audio_sampling_frequency = request.form['audio_sampling_frequency']
        fname = request.files['img']  # 获取上传的文件
        pattern1 = re.compile(r'(.*\.mp4)')
        match1 = pattern1.match(fname.filename)
        if match1:
            hou='.mp4'
        pattern2 = re.compile(r'(.*\.3gp)')
        match2 = pattern2.match(fname.filename)
        if match2:
            hou='.3gp'
        pattern3 = re.compile(r'(.*\.wmv)')
        match3 = pattern3.match(fname.filename)
        if match3:
            hou='.wmv'
        pattern4 = re.compile(r'(.*\.avi)')
        match4 = pattern4.match(fname.filename)
        if match4:
            hou='.avi'
        pattern5 = re.compile(r'(.*\.fiv)')
        match5 = pattern5.match(fname.filename)
        if match5:
            hou='.fiv'
        strr= time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        if (match1 or match2 or match3 or match4 or match5):
            if (series == '剧目'):
                new_fname = r'watchlist/static/resource/dramas/'+ strr +hou
                fname.save(new_fname)  # 保存文件到指定路径
                f = open(new_fname, "rb")
                strx = int(len(f.read()))
                strx = strx / 1024
                if (strx > 1024):
                    str2 = strx / 1024
                    str2 = round(str2, 1)
                    str1 = str(str2) + 'mb'
                else:
                    if (strx % 1 == 0):
                        strx = int(strx)
                        str1 = str(strx) + 'kb'
                    else:
                        strx = round(strx, 1)
                        str1 = str(strx) + 'kb'
                flash('Item created.')  # 显示成功创建的提示
                URL = 'resource/dramas/'+strr+hou
            else:
                new_fname = r'watchlist/static/resource/instructions/' +strr+ hou
                fname.save(new_fname)  # 保存文件到指定路径
                f = open(new_fname, "rb")
                strx = int(len(f.read()))
                strx = strx / 1024
                if (strx > 1024):
                    str2 = strx / 1024
                    str2 = round(str2, 1)
                    str1 = str(str2) + 'mb'
                else:
                    if (strx % 1 == 0):
                        strx = int(strx)
                        str1 = str(strx) + 'kb'
                    else:
                        strx = round(strx, 1)
                        str1 = str(strx) + 'kb'
                flash('Item created.')  # 显示成功创建的提示
                URL = 'resource/instructions/'+strr+hou
        else:
            flash('Date format error.')
            return render_template('addvideo.html')
        create_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        video = Videos(title=title, URL=URL, series=series, parallel_title=parallel_title,
                          alternate_title=alternate_title, other_title_info=other_title_info, series_title=series_title,
                          parallel_series_title=parallel_series_title, individual_name=individual_name,
                          group_name=group_name, conference_name=conference_name, joint_author_name=joint_author_name,
                          other_info=other_info, bearing_method=bearing_method, version=version, public_date=public_date,
                          addi_block_type=addi_block_type, addi_block_desc=addi_block_desc, sound_id=sound_id,
                          sound_content=sound_content, notes=notes, search_method=search_method, key_word=key_word, sum=sum,
                          system=system, sound_chara=sound_chara, colors=colors, resolution=resolution, sound_qua=sound_qua,
                          frame_qua=frame_qua, mode=mode, type=hou, depth=depth,
                          video_sampling_frequency=video_sampling_frequency, language_id=language_id,
                          language_type=language_type, subtitle_id=subtitle_id, subtitle_type=subtitle_type,
                          audience=audience, ori_form=ori_form, other_form=other_form, inclusion=inclusion,
                          included=included, refering=refering, reference=reference, copyright_holder=copyright_holder,
                          copyright_notice=copyright_notice, authorize_person=authorize_person, authorize_form=authorize_form,
                          authorize_date=authorize_date, authorize_due=authorize_due, authorize_area=authorize_area,
                          authorize_file=authorize_file, authorize_info=authorize_info, time_length=time_length,
                          space_length=space_length, source_carrier=source_carrier, collect_area=collect_area,
                          collect_unit=collect_unit, call_number=call_number, collect_person=collect_person,
                          process_unit=process_unit, serve_form=serve_form, serve_column=serve_column,
                          serve_time=serve_time, serve_addr=serve_addr, serve_obj=serve_obj, acce_time=acce_time,
                          acce_form=acce_form, acce_person=acce_person, acce_opi=acce_opi, acce_repo=acce_repo,
                          episode=episode,
                          total_episodes=total_episodes,
                          producer=producer, pro_loca=pro_loca, resource=resource, provider=provider,
                          video_date=video_date, create_date=create_date, release_date=release_date, award=award,
                          performance_form=performance_form, program_type=program_type, subtitle=subtitle,
                          length=length, aspect_ratio=aspect_ratio, bit_rate=bit_rate, sound_track=sound_track,
                          data_rate=data_rate, total_bitrate=total_bitrate,
                          audio_sampling_frequency=audio_sampling_frequency, size=str1)  # 创建记录
        db.session.add(video)  # 添加到数据库会话
        db.session.commit()  # 提交数据库会话
        flash('Item created.')  # 显示成功创建的提示
        if (video.series == "教程"):
            user = User.query.first()  # 读取用户记录
            instructions = Videos.query.filter(Videos.series == "教程").order_by(Videos.create_date.desc())
            return render_template('indexinstruction.html', user=user, instructions=instructions)
        else:
            user = User.query.first()  # 读取用户记录
            dramas = Videos.query.filter(Videos.series == "剧目").order_by(Videos.create_date.desc())
            return render_template('indexdrama.html', user=user, dramas=dramas)
    return render_template('addvideo.html')

@app.route('/videodelete<int:video_id>', methods=['POST'])
@login_required
def deletev(video_id):
    video = Videos.query.get_or_404(video_id)
    db.session.delete(video)
    db.session.commit()
    flash('Item deleted.')
    if(video.series=="教程"):
        user = User.query.first()  # 读取用户记录
        instructions = Videos.query.filter(Videos.series == "教程").order_by(Videos.create_date.desc())
        return render_template('indexinstruction.html', user=user, instructions=instructions)
    else:
        user = User.query.first()  # 读取用户记录
        dramas = Videos.query.filter(Videos.series == "剧目").order_by(Videos.create_date.desc())
        return render_template('indexdrama.html', user=user, dramas=dramas)


@app.route('/picturedelete<int:picture_id>', methods=['POST'])
@login_required
def deletep(picture_id):
    picture = Pictures.query.get_or_404(picture_id)
    db.session.delete(picture)
    db.session.commit()
    flash('Item deleted.')
    user = User.query.first()  # 读取用户记录
    pics = Pictures.query.order_by(Pictures.create_date.desc()).all()  # 图片
    return render_template('indexpicture.html', user=user, pictures=pics)


@app.route('/recorddelete<int:record_id>', methods=['POST'])
@login_required
def deleter(record_id):
    record = Records.query.get_or_404(record_id)
    db.session.delete(record)
    db.session.commit()
    flash('Item deleted.')
    user = User.query.first()  # 读取用户记录
    musics = Records.query.order_by(Records.create_date.desc()).all()  # 音频
    return render_template('indexmusic.html', user=user, musics=musics)

@app.route('/documentdelete<int:document_id>', methods=['POST'])
@login_required
def deleted(document_id):
    document = Documents.query.get_or_404(document_id)
    db.session.delete(document)
    db.session.commit()
    flash('Item deleted.')
    user = User.query.first()  # 读取用户记录
    documents = Documents.query.order_by(Documents.create_date.desc()).all()  # 文本
    return render_template('indexdocument.html', user=user, documents=documents)

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form['name']

        if not name or len(name) > 20:
            flash('Invalid input.')
            return redirect(url_for('settings'))

        user = User.query.first()
        user.name = name
        db.session.commit()
        flash('Settings updated.')
        return redirect(url_for('index'))

    return render_template('settings.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Invalid input.')
            return redirect(url_for('login'))

        user = User.query.first()

        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('Login success.')
            return redirect(url_for('index'))

        flash('Invalid username or password.')
        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Goodbye.')
    return redirect(url_for('index'))

