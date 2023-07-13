from datetime import datetime

HOUR_DATE = "%I:%M:%S %d/%m/%y"


class Timestamp:
    def __init__(self, timestamp: str = None):
        self.timestamp = datetime.strftime(datetime.fromisoformat(timestamp), HOUR_DATE)

    def __str__(self):
        return self.timestamp


class DanbooruAPI:
    def __init__(self,
                 api_name: str = None,
                 api_key: str = None,
                 api_uses: int = None,
                 api_last_use: str = None,
                 api_created: str = None):
        self.api_name = api_name
        self.api_key = api_key
        self.api_uses = api_uses
        self.api_last_use = api_last_use
        self.api_created = api_created

    def __str__(self):
        return str(self.__dict__())

    def __dict__(self):
        return {
            "api_name": self.api_name,
            "api_key": self.api_key,
            "api_uses": self.api_uses,
            "api_last_use": self.api_uses,
            "api_created": self.api_created
        }


class DEB:
    def __init__(self,
                 success: bool = None,
                 error: str = None,
                 message: str = None,
                 backtrace: list = None
                 ):
        self.success = success
        self.error = error
        self.message = message
        self.backtrace = backtrace

    def __str__(self):
        return str(self.__dict__())

    def __dict__(self):
        return {
            "success": self.success,
            "message": self.message,
            "backtrace": self.backtrace
        }


class DanbooruAccount:
    def __init__(self,
                 _id: int = None,
                 name: str = None,
                 level: int = None,
                 inviter_id: int = None,
                 created_at: str = None,
                 last_logged_in_at: str = None,
                 last_forum_read_at: str = None,
                 comment_threshold: int = None,
                 updated_at: int = None,
                 default_image_size: str = None,
                 favorite_tags: str = None,
                 blacklisted_tags: str = None,
                 time_zone: str = None,
                 post_update_count: int = None,
                 note_update_count: int = None,
                 favorite_count: int = None,
                 post_upload_count: int = None,
                 per_page: int = None,
                 custom_style: str = None,
                 theme: str = None,
                 is_deleted: bool = None,
                 is_banned: bool = None,
                 can_approve_posts: bool = None,
                 can_upload_free: bool = None,
                 level_string: str = None,
                 _unused_has_mail: bool = None,
                 receive_email_notifications: bool = None,
                 _unused_always_resize_images: bool = None,
                 _unused_enable_post_navigation: bool = None,
                 new_post_navigation_layout: bool = None,
                 enable_private_favorites: bool = None,
                 _unused_enable_sequential_post_navigation: bool = None,
                 _unused_hide_deleted_posts: bool = None,
                 style_usernames: bool = None,
                 _unused_enable_auto_complete: bool = None,
                 show_deleted_children: bool = None,
                 _unused_has_saved_searches: bool = None,
                 disable_categorized_saved_searches: bool = None,
                 _unused_is_super_voter: bool = None,
                 disable_tagged_filenames: bool = None,
                 _unused_enable_recent_searches: bool = None,
                 _unused_disable_cropped_thumbnails: bool = None,
                 disable_mobile_gestures: bool = None,
                 enable_safe_mode: bool = None,
                 enable_desktop_mode: bool = None,
                 disable_post_tooltips: bool = None,
                 _unused_enable_recommended_posts: bool = None,
                 _unused_opt_out_tracking: bool = None,
                 _unused_no_flagging: bool = None,
                 _unused_no_feedback: bool = None,
                 requires_verification: bool = None,
                 is_verified: bool = None,
                 show_deleted_posts: bool = None,
                 statement_timeout: int = None,
                 favorite_group_limit: int = None,
                 tag_query_limit: int = None,
                 max_saved_searches: int = None,
                 wiki_page_version_count: int = None,
                 artist_version_count: int = None,
                 artist_commentary_version_count: int = None,
                 pool_version_count: int = None,
                 forum_post_count: int = None,
                 comment_count: int = None,
                 favorite_group_count: int = None,
                 appeal_count: int = None,
                 flag_count: int = None,
                 positive_feedback_count: int = None,
                 neutral_feedback_count: int = None,
                 negative_feedback_count: int = None
                 ):
        self.id = _id
        self.name = name
        self.level = level
        self.inviter_id = inviter_id
        self.created_at = created_at
        self.last_logged_in_at = last_logged_in_at
        self.last_forum_read_at = last_forum_read_at
        self.comment_threshold = comment_threshold
        self.updated_at = updated_at
        self.default_image_size = default_image_size
        self.favorite_tags = favorite_tags
        self.blacklisted_tags = blacklisted_tags
        self.time_zone = time_zone
        self.post_update_count = post_update_count
        self.note_update_count = note_update_count
        self.favorite_count = favorite_count
        self.post_upload_count = post_upload_count
        self.per_page = per_page
        self.custom_style = custom_style
        self.theme = theme
        self.is_banned = is_banned
        self.can_approve_posts = can_approve_posts
        self.can_upload_free = can_upload_free
        self.level_string = level_string
        self._unused_has_mail = _unused_has_mail
        self.receive_email_notifications = receive_email_notifications
        self._unused_always_resize_images = _unused_always_resize_images
        self._unused_enable_post_navigation = _unused_enable_post_navigation
        self.new_post_navigation_layout = new_post_navigation_layout
        self.enable_private_favorites = enable_private_favorites
        self._unused_enable_sequential_post_navigation = _unused_enable_sequential_post_navigation
        self._unused_hide_deleted_posts = _unused_hide_deleted_posts
        self.style_usernames = style_usernames
        self._unused_enable_auto_complete = _unused_enable_auto_complete
        self.show_deleted_children = show_deleted_children
        self._unused_has_saved_searches = _unused_has_saved_searches
        self.disable_categorized_saved_searches = disable_categorized_saved_searches
        self._unused_is_super_voter = _unused_is_super_voter
        self.disable_tagged_filenames = disable_tagged_filenames
        self._unused_enable_recent_searches = _unused_enable_recent_searches
        self._unused_disable_cropped_thumbnails = _unused_disable_cropped_thumbnails
        self.disable_mobile_gestures = disable_mobile_gestures
        self.enable_safe_mode = enable_safe_mode
        self.enable_desktop_mode = enable_desktop_mode
        self.disable_post_tooltips = disable_post_tooltips
        self._unused_enable_recommended_posts = _unused_enable_recommended_posts
        self._unused_opt_out_tracking = _unused_opt_out_tracking
        self._unused_no_flagging = _unused_no_flagging
        self._unused_no_feedback = _unused_no_feedback
        self.requires_verification = requires_verification
        self.is_verified = is_verified
        self.show_deleted_posts = show_deleted_posts
        self.statement_timeout = statement_timeout
        self.favorite_group_limit = favorite_group_limit
        self.tag_query_limit = tag_query_limit
        self.max_saved_searches = max_saved_searches
        self.wiki_page_version_count = wiki_page_version_count
        self.artist_version_count = artist_version_count
        self.artist_commentary_version_count = artist_commentary_version_count
        self.pool_version_count = pool_version_count
        self.forum_post_count = forum_post_count
        self.comment_count = comment_count
        self.favorite_group_count = favorite_group_count
        self.appeal_count = appeal_count
        self.flag_count = flag_count
        self.positive_feedback_count = positive_feedback_count
        self.neutral_feedback_count = neutral_feedback_count
        self.negative_feedback_count = negative_feedback_count

    def __str__(self):
        return str(self.__dict__())

    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name,
            "level": self.level,
            "inviter_id": self.inviter_id,
            "created_at": self.created_at,
            "last_logged_in_at": self.last_logged_in_at,
            "last_forum_read_at": self.last_forum_read_at,
            "comment_threshold": self.comment_threshold,
            "updated_at": self.updated_at,
            "default_image_size": self.default_image_size,
            "favorite_tags": self.favorite_tags,
            "blacklisted_tags": self.blacklisted_tags,
            "time_zone": self.time_zone,
            "post_update_count": self.post_update_count,
            "note_update_count": self.note_update_count,
            "favorite_count": self.favorite_count,
            "post_upload_count": self.post_upload_count,
            "per_page": self.per_page,
            "custom_style": self.custom_style,
            "theme": self.theme,
            "is_banned": self.is_banned,
            "can_approve_posts": self.can_approve_posts,
            "can_upload_free": self.can_upload_free,
            "level_string": self.level_string,
            "_unused_has_mail": self._unused_has_mail,
            "receive_email_notifications": self.receive_email_notifications,
            "_unused_always_resize_images": self._unused_always_resize_images,
            "_unused_enable_post_navigation": self._unused_enable_post_navigation,
            "new_post_navigation_layout": self.new_post_navigation_layout,
            "enable_private_favorites": self.enable_private_favorites,
            "_unused_enable_sequential_post_navigation": self._unused_enable_sequential_post_navigation,
            "_unused_hide_deleted_posts": self._unused_hide_deleted_posts,
            "style_usernames": self.style_usernames,
            "_unused_enable_auto_complete": self._unused_enable_auto_complete,
            "show_deleted_children": self.show_deleted_children,
            "_unused_has_saved_searches": self._unused_has_saved_searches,
            "disable_categorized_saved_searches": self.disable_categorized_saved_searches,
            "_unused_is_super_voter": self._unused_is_super_voter,
            "disable_tagged_filenames": self.disable_tagged_filenames,
            "_unused_enable_recent_searches": self._unused_enable_recent_searches,
            "_unused_disable_cropped_thumbnails": self._unused_disable_cropped_thumbnails,
            "disable_mobile_gestures": self.disable_mobile_gestures,
            "enable_safe_mode": self.enable_safe_mode,
            "enable_desktop_mode": self.enable_desktop_mode,
            "disable_post_tooltips": self.disable_post_tooltips,
            "_unused_enable_recommended_posts": self._unused_enable_recommended_posts,
            "_unused_opt_out_tracking": self._unused_opt_out_tracking,
            "_unused_no_flagging": self._unused_no_flagging,
            "_unused_no_feedback": self._unused_no_feedback,
            "requires_verification": self.requires_verification,
            "is_verified": self.is_verified,
            "show_deleted_posts": self.show_deleted_posts,
            "statement_timeout": self.statement_timeout,
            "favorite_group_limit": self.favorite_group_limit,
            "tag_query_limit": self.tag_query_limit,
            "max_saved_searches": self.max_saved_searches,
            "wiki_page_version_count": self.wiki_page_version_count,
            "artist_version_count": self.artist_version_count,
            "artist_commentary_version_count": self.artist_commentary_version_count,
            "pool_version_count": self.pool_version_count,
            "forum_post_count": self.forum_post_count,
            "comment_count": self.comment_count,
            "favorite_group_count": self.favorite_group_count,
            "appeal_count": self.appeal_count,
            "flag_count": self.flag_count,
            "positive_feedback_count": self.positive_feedback_count,
            "neutral_feedback_count": self.neutral_feedback_count,
            "negative_feedback_count": self.negative_feedback_count
        }


class PostInfo:
    def __init__(self,
                 _id: int = None,
                 created_at: str = None,
                 uploader_id: int = None,
                 score: int = None,
                 source: str = None,
                 md5: str = None,
                 last_comment_bumped_at: str = None,
                 rating: str = None,
                 image_width: int = None,
                 image_height: int = None,
                 tag_string: str = None,
                 is_note_locked: bool = None,
                 fav_count: int = None,
                 file_ext: str = None,
                 last_noted_at: str = None,
                 is_rating_locked: bool = None,
                 parent_id: int = None,
                 has_children: bool = None,
                 approver_id: int = None,
                 tag_count_general: int = None,
                 tag_count_artist: int = None,
                 tag_count_character: int = None,
                 tag_count_copyright: int = None,
                 file_size: int = None,
                 is_status_locked: bool = None,
                 up_score: int = None,
                 down_score: int = None,
                 is_pending: bool = None,
                 is_flagged: bool = None,
                 is_deleted: bool = None,
                 tag_count: int = None,
                 updated_at: str = None,
                 is_banned: bool = None,
                 pixiv_id: int = None,
                 last_commented_at: str = None,
                 has_active_children: bool = None,
                 bit_flags: int = None,
                 tag_count_meta: int = None,
                 has_large: bool = None,
                 has_visible_children: bool = None,
                 media_asset: dict = None,
                 tag_string_general: str = None,
                 tag_string_character: str = None,
                 tag_string_copyright: str = None,
                 tag_string_artist: str = None,
                 tag_string_meta: str = None,
                 file_url: str = None,
                 large_file_url: str = None,
                 preview_file_url: str = None):
        self.id = _id
        self.created_at = created_at
        self.uploader_id = uploader_id
        self.score = score
        self.source = source
        self.md5 = md5
        self.last_comment_bumped_at = last_comment_bumped_at
        self.rating = rating
        self.image_width = image_width
        self.image_height = image_height
        self.tag_string = tag_string
        self.is_note_locked = is_note_locked
        self.fav_count = fav_count
        self.file_ext = file_ext
        self.last_noted_at = last_noted_at
        self.is_rating_locked = is_rating_locked
        self.parent_id = parent_id
        self.has_children = has_children
        self.approver_id = approver_id
        self.tag_count_general = tag_count_general
        self.tag_count_artist = tag_count_artist
        self.tag_count_character = tag_count_character
        self.tag_count_copyright = tag_count_copyright
        self.file_size = file_size
        self.is_status_locked = is_status_locked
        self.up_score = up_score
        self.down_score = down_score
        self.is_pending = is_pending
        self.is_flagged = is_flagged
        self.is_deleted = is_deleted
        self.tag_count = tag_count
        self.updated_at = updated_at
        self.is_banned = is_banned
        self.pixiv_id = pixiv_id
        self.last_commented_at = last_commented_at
        self.has_active_children = has_active_children
        self.bit_flags = bit_flags
        self.tag_count_meta = tag_count_meta
        self.has_large = has_large
        self.has_visible_children = has_visible_children
        self.tag_string_general = tag_string_general
        self.tag_string_character = tag_string_character
        self.tag_string_copyright = tag_string_copyright
        self.tag_string_artist = tag_string_artist
        self.tag_string_meta = tag_string_meta
        self.file_url = file_url
        self.large_file_url = large_file_url
        self.preview_file_url = preview_file_url

    def __str__(self):
        return str(self.__dict__())

    def __dict__(self):
        return {
            "id": self.id,
            "created_at": self.created_at,
            "uploader_id": self.uploader_id,
            "score": self.score,
            "source": self.source,
            "md5": self.md5,
            "last_comment_bumped_at": self.last_comment_bumped_at,
            "rating": self.rating,
            "image_width": self.image_width,
            "image_height": self.image_height,
            "tag_string": self.tag_string,
            "is_note_locked": self.is_note_locked,
            "fav_count": self.fav_count,
            "file_ext": self.file_ext,
            "last_noted_at": self.last_noted_at,
            "is_rating_locked": self.is_rating_locked,
            "parent_id": self.parent_id,
            "has_children": self.has_children,
            "approver_id": self.approver_id,
            "tag_count_general": self.tag_count_general,
            "tag_count_artist": self.tag_count_artist,
            "tag_count_character": self.tag_count_character,
            "tag_count_copyright": self.tag_count_copyright,
            "file_size": self.file_size,
            "is_status_locked": self.is_status_locked,
            "up_score": self.up_score,
            "down_score": self.down_score,
            "is_pending": self.is_pending,
            "is_flagged": self.is_flagged,
            "is_deleted": self.is_deleted,
            "tag_count": self.tag_count,
            "updated_at": self.updated_at,
            "is_banned": self.is_banned,
            "pixiv_id": self.pixiv_id,
            "last_commented_at": self.last_commented_at,
            "has_active_children": self.has_active_children,
            "bit_flags": self.bit_flags,
            "tag_count_meta": self.tag_count_meta,
            "has_large": self.has_large,
            "has_visible_children": self.has_visible_children,
            "tag_string_general": self.tag_string_general,
            "tag_string_character": self.tag_string_character,
            "tag_string_copyright": self.tag_string_copyright,
            "tag_string_artist": self.tag_string_artist,
            "tag_string_meta": self.tag_string_meta,
            "file_url": self.file_url,
            "large_file_url": self.large_file_url,
            "preview_file_url": self.preview_file_url
        }


# def post_info(function):
#     def wrapper(
#             self,
#             tags: str = None,
#             page: int = 1,
#             limit: int = 100,
#             md5: str = None,
#             random: bool = False,
#             raw: bool = False
#     ):
#         return function(
#             self=self,
#             tags=tags,
#             page=page,
#             limit=limit,
#             md5=md5,
#             random=random,
#             raw=raw
#         )
#     return wrapper




