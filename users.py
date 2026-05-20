# SECURE: Adding authorization context
@app.route('/api/profile/<int:user_id>')
@login_required
def view_profile(user_id):
    if current_user.id != user_id and not current_user.is_admin:
        return abort(403, description="Unauthorized access")
    
    user = User.query.get(user_id)
    return jsonify(user.sensitive_data) if user else abort(404)